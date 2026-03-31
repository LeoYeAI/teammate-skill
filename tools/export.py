#!/usr/bin/env python3
"""
Teammate Export

Creates a portable, privacy-checked package for sharing teammate skills.
Exports only the generated skill files (not raw knowledge/source data).

Usage:
    python3 export.py --slug alex-chen --base-dir ./teammates
    python3 export.py --slug alex-chen --base-dir ./teammates --include-knowledge
    python3 export.py --slug alex-chen --base-dir ./teammates --output /tmp/alex-chen.teammate.tar.gz
"""

from __future__ import annotations

import json
import tarfile
import argparse
import sys
import io
from pathlib import Path
from datetime import datetime, timezone


def export_teammate(slug: str, base_dir: str, output: str = None, include_knowledge: bool = False):
    """Export a teammate skill as a portable tar.gz package."""
    skill_dir = Path(base_dir) / slug

    if not skill_dir.exists():
        print(f"❌ Teammate '{slug}' not found at {skill_dir}")
        sys.exit(1)

    meta_path = skill_dir / "meta.json"
    if not meta_path.exists():
        print(f"❌ No meta.json found for '{slug}'")
        sys.exit(1)

    meta = json.loads(meta_path.read_text(encoding="utf-8"))

    # Determine output path
    if not output:
        output = f"./{slug}.teammate.tar.gz"
    output_path = Path(output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Files to include (skill files only, no raw knowledge by default)
    include_files = []

    # Core skill files
    for fname in ["SKILL.md", "work.md", "persona.md", "meta.json"]:
        fpath = skill_dir / fname
        if fpath.exists():
            include_files.append((fpath, f"{slug}/{fname}"))

    # Version history (lightweight — meta only)
    versions_dir = skill_dir / "versions"
    if versions_dir.exists():
        for v_dir in sorted(versions_dir.iterdir()):
            if v_dir.is_dir():
                for f in v_dir.iterdir():
                    if f.is_file():
                        include_files.append((f, f"{slug}/versions/{v_dir.name}/{f.name}"))

    # Knowledge files (only if explicitly requested)
    if include_knowledge:
        knowledge_dir = skill_dir / "knowledge"
        if knowledge_dir.exists():
            for f in knowledge_dir.rglob("*"):
                if f.is_file():
                    rel = f.relative_to(skill_dir)
                    include_files.append((f, f"{slug}/{rel}"))
        print("⚠️  Including knowledge files — these may contain personal messages and PII.")
        print("   Run privacy_guard.py --scan --redact before sharing publicly.")

    # Add export manifest
    manifest = {
        "format": "teammate.skill/v1",
        "slug": slug,
        "name": meta.get("name", slug),
        "version": meta.get("version", "v1"),
        "exported_at": datetime.now(timezone.utc).isoformat(),
        "includes_knowledge": include_knowledge,
        "file_count": len(include_files),
        "profile": meta.get("profile", {}),
        "tags": meta.get("tags", {}),
    }

    # Create tar.gz
    with tarfile.open(output_path, "w:gz") as tar:
        # Add manifest
        manifest_bytes = json.dumps(manifest, indent=2, ensure_ascii=False).encode("utf-8")
        info = tarfile.TarInfo(name=f"{slug}/manifest.json")
        info.size = len(manifest_bytes)
        tar.addfile(info, io.BytesIO(manifest_bytes))

        # Add files
        for file_path, archive_name in include_files:
            tar.add(str(file_path), arcname=archive_name)

    # Size report
    size_bytes = output_path.stat().st_size
    if size_bytes < 1024:
        size_str = f"{size_bytes} B"
    elif size_bytes < 1024 * 1024:
        size_str = f"{size_bytes / 1024:.1f} KB"
    else:
        size_str = f"{size_bytes / (1024 * 1024):.1f} MB"

    print(f"\n✅ Exported '{slug}' → {output_path}")
    print(f"   Version: {manifest['version']}")
    print(f"   Files: {len(include_files) + 1}")  # +1 for manifest
    print(f"   Size: {size_str}")
    print(f"   Knowledge: {'included ⚠️' if include_knowledge else 'excluded (safe to share)'}")

    print(f"\n📦 Import on another machine:")
    print(f"   tar xzf {output_path.name} -C ./teammates/")
    print(f"   Then copy {slug}/SKILL.md to your agent's skill directory.")


def import_teammate(archive: str, base_dir: str):
    """Import a teammate skill from a tar.gz package."""
    archive_path = Path(archive)
    if not archive_path.exists():
        print(f"❌ File not found: {archive_path}")
        sys.exit(1)

    base = Path(base_dir)
    base.mkdir(parents=True, exist_ok=True)

    with tarfile.open(archive_path, "r:gz") as tar:
        # Safety check: no path traversal
        for member in tar.getmembers():
            if member.name.startswith("/") or ".." in member.name:
                print(f"❌ Unsafe path in archive: {member.name}")
                sys.exit(1)

        # Check manifest
        manifest = None
        for member in tar.getmembers():
            if member.name.endswith("manifest.json"):
                f = tar.extractfile(member)
                if f:
                    manifest = json.loads(f.read().decode("utf-8"))
                break

        if not manifest:
            print("⚠️  No manifest found — this may not be a teammate.skill package.")

        tar.extractall(path=str(base))

    slug = manifest["slug"] if manifest else archive_path.stem.replace(".teammate", "")
    print(f"\n✅ Imported '{slug}' to {base / slug}/")
    if manifest:
        print(f"   Name: {manifest.get('name', 'unknown')}")
        print(f"   Version: {manifest.get('version', 'unknown')}")
        print(f"   Files: {manifest.get('file_count', '?')}")


def main():
    parser = argparse.ArgumentParser(description="Export/import teammate skills")
    parser.add_argument("--slug", help="Teammate slug to export")
    parser.add_argument("--base-dir", default="./teammates", help="Base directory")
    parser.add_argument("--output", help="Output file path")
    parser.add_argument("--include-knowledge", action="store_true",
                        help="Include raw knowledge files (contains PII)")
    parser.add_argument("--import-file", help="Import from a .teammate.tar.gz file")

    args = parser.parse_args()

    if args.import_file:
        import_teammate(args.import_file, args.base_dir)
    elif args.slug:
        export_teammate(args.slug, args.base_dir, args.output, args.include_knowledge)
    else:
        parser.error("Either --slug (export) or --import-file (import) is required")


if __name__ == "__main__":
    main()
