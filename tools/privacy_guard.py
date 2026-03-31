#!/usr/bin/env python3
"""
Privacy Guard

Scans generated skill files and knowledge directories for potential PII,
secrets, and sensitive data. Can redact or warn.

Usage:
    python3 privacy_guard.py --scan ./teammates/alex-chen/
    python3 privacy_guard.py --scan ./teammates/alex-chen/ --redact
    python3 privacy_guard.py --scan ./knowledge/alex-chen/
"""

from __future__ import annotations

import re
import argparse
import sys
from pathlib import Path
from typing import NamedTuple


class Finding(NamedTuple):
    file: str
    line: int
    category: str
    matched: str
    suggestion: str


# Patterns for PII and secrets detection
PATTERNS = [
    # Emails
    (r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
     'email', '[EMAIL_REDACTED]'),
    # Phone numbers (various formats)
    (r'\b(?:\+?1[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b',
     'phone', '[PHONE_REDACTED]'),
    # IP addresses (not localhost/private ranges in some cases)
    (r'\b(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\b',
     'ip_address', '[IP_REDACTED]'),
    # AWS keys
    (r'\b(?:AKIA|ASIA)[A-Z0-9]{16}\b',
     'aws_key', '[AWS_KEY_REDACTED]'),
    # Generic API keys / tokens (long hex or base64 strings)
    (r'\b(?:sk-|pk-|xoxb-|xoxp-|ghp_|gho_|glpat-)[A-Za-z0-9_-]{20,}\b',
     'api_token', '[TOKEN_REDACTED]'),
    # SSN (US)
    (r'\b\d{3}-\d{2}-\d{4}\b',
     'ssn', '[SSN_REDACTED]'),
    # Credit card numbers (basic)
    (r'\b(?:\d{4}[-\s]?){3}\d{4}\b',
     'credit_card', '[CARD_REDACTED]'),
    # Slack webhook URLs
    (r'https://hooks\.slack\.com/services/[A-Za-z0-9/]+',
     'slack_webhook', '[WEBHOOK_REDACTED]'),
    # Private keys
    (r'-----BEGIN (?:RSA |EC )?PRIVATE KEY-----',
     'private_key', '[PRIVATE_KEY_REDACTED]'),
    # Passwords in common formats
    (r'(?i)(?:password|passwd|pwd)\s*[:=]\s*["\']?[^\s"\']{8,}',
     'password', '[PASSWORD_REDACTED]'),
]

# Compile patterns
COMPILED_PATTERNS = [(re.compile(p), cat, sub) for p, cat, sub in PATTERNS]

# File extensions to scan
SCANNABLE_EXTENSIONS = {'.md', '.txt', '.json', '.py', '.yml', '.yaml', '.csv', '.html', '.xml'}


def scan_file(file_path: Path) -> list[Finding]:
    """Scan a single file for PII and sensitive data."""
    findings = []
    try:
        content = file_path.read_text(encoding='utf-8', errors='replace')
    except Exception:
        return findings

    for line_num, line in enumerate(content.splitlines(), 1):
        for pattern, category, suggestion in COMPILED_PATTERNS:
            for match in pattern.finditer(line):
                matched_text = match.group()
                # Skip common false positives
                if category == 'phone' and len(matched_text.replace('-', '').replace('.', '').replace(' ', '')) < 10:
                    continue
                if category == 'ip_address' and matched_text in ('127.0.0.1', '0.0.0.0', '255.255.255.255'):
                    continue
                if category == 'credit_card' and matched_text.replace('-', '').replace(' ', '') in ('0000000000000000',):
                    continue

                findings.append(Finding(
                    file=str(file_path),
                    line=line_num,
                    category=category,
                    matched=matched_text[:50] + ('...' if len(matched_text) > 50 else ''),
                    suggestion=suggestion,
                ))

    return findings


def scan_directory(dir_path: Path) -> list[Finding]:
    """Recursively scan a directory for PII."""
    all_findings = []
    for file_path in sorted(dir_path.rglob('*')):
        if not file_path.is_file():
            continue
        if file_path.suffix.lower() not in SCANNABLE_EXTENSIONS:
            continue
        # Skip version archives
        if '/versions/' in str(file_path):
            continue
        all_findings.extend(scan_file(file_path))
    return all_findings


def redact_file(file_path: Path, findings: list[Finding]) -> int:
    """Redact findings in a file. Returns count of redactions."""
    if not findings:
        return 0

    content = file_path.read_text(encoding='utf-8', errors='replace')
    redaction_count = 0

    for pattern, category, substitution in COMPILED_PATTERNS:
        new_content, count = pattern.subn(substitution, content)
        if count > 0:
            content = new_content
            redaction_count += count

    file_path.write_text(content, encoding='utf-8')
    return redaction_count


def main():
    parser = argparse.ArgumentParser(description='Scan for PII and sensitive data in teammate files')
    parser.add_argument('--scan', required=True, help='Directory or file to scan')
    parser.add_argument('--redact', action='store_true', help='Auto-redact findings (modifies files)')
    parser.add_argument('--json', action='store_true', help='Output as JSON')

    args = parser.parse_args()
    scan_path = Path(args.scan)

    if not scan_path.exists():
        print(f'❌ Path not found: {scan_path}')
        sys.exit(1)

    # Scan
    if scan_path.is_dir():
        findings = scan_directory(scan_path)
    else:
        findings = scan_file(scan_path)

    if not findings:
        print('✅ No PII or sensitive data detected.')
        return

    # Report
    print(f'\n⚠️  Found {len(findings)} potential sensitive item(s):\n')

    by_category = {}
    for f in findings:
        by_category.setdefault(f.category, []).append(f)

    for category, items in sorted(by_category.items()):
        print(f'  {category}: {len(items)} occurrence(s)')
        for item in items[:3]:  # Show first 3 per category
            print(f'    → {item.file}:{item.line} — {item.matched}')
        if len(items) > 3:
            print(f'    ... and {len(items) - 3} more')
    print()

    # Redact if requested
    if args.redact:
        files_to_redact = {}
        for f in findings:
            files_to_redact.setdefault(f.file, []).append(f)

        total_redactions = 0
        for file_path_str, file_findings in files_to_redact.items():
            count = redact_file(Path(file_path_str), file_findings)
            total_redactions += count
            if count > 0:
                print(f'  ✏️  Redacted {count} item(s) in {file_path_str}')

        print(f'\n✅ Redacted {total_redactions} item(s) total.')
    else:
        print('Run with --redact to auto-redact these findings.')
        print('Or review manually and remove sensitive data before sharing.')


if __name__ == '__main__':
    main()
