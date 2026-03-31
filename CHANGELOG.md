# Changelog

All notable changes to teammate.skill are documented here.

## [2.0.0] — 2026-03-31

### 🎯 Quality Pipeline — the biggest upgrade

Every teammate now goes through a **3-layer quality pipeline** before delivery:

1. **Quality Gate** — 7-point mandatory self-check before showing the preview. Validates Layer 0 concreteness (no bare adjectives), example count, catchphrase density, priority ordering, work scope, generic filler detection, and tag→rule translation completeness. Failures auto-fix before you see anything.

2. **Smoke Test** — 3 automated test prompts run against every generated skill post-creation:
   - Domain question: does the skill use real systems, not generic advice?
   - Pushback scenario: does the persona hold under pressure?
   - Out-of-scope: does the skill admit limits in-character?

3. **Privacy Scan** — PII detection (emails, phones, API tokens, SSNs, credit cards, private keys) with one-command auto-redaction.

### 🆕 New Commands

- **`/compare {slug1} vs {slug2}`** — Side-by-side teammate comparison with:
  - General overview (10-dimension contrast table)
  - Scenario-based analysis ("who should review this?")
  - Decision simulation (watch two teammates debate in character)

- **`/export-teammate {slug}`** — Portable `.tar.gz` packages for sharing:
  - Includes SKILL.md, work.md, persona.md, meta.json, version history
  - Raw knowledge files excluded by default (privacy-safe)
  - Import on any machine with `tar xzf`
  - Manifest with format version for forward compatibility

### 🛡️ Production Hardening

- **Slack Collector**: Full cursor-based pagination (was limited to 200 channels, single page per channel). Exponential backoff on 429 rate limits with Retry-After header support. Progress indicator every 5 channels.

- **GitHub Collector**: Retry up to 3x on rate limit with X-RateLimit-Reset header. 404 returns empty list instead of crashing (private repos). Wait capped at 5 minutes per retry.

- **Generated SKILL.md**: Added 3 defensive execution rules — "never break character into generic AI", "don't fabricate expertise they don't have", "keep response length realistic for this person's style".

- **Skill Writer (update_skill)**: Patches now insert before Correction Log (not naive EOF append). Update history tracked in meta.json (last 20 entries). Output shows which files changed.

### 🧠 Smarter Analysis

- **3-tier data volume strategy** for both persona_analyzer and work_analyzer:
  - Tier 1 (profile only): tag-inferred, clearly labeled, no fabricated quotes
  - Tier 2 (light data): evidenced vs inferred distinction for correction targeting  
  - Tier 3 (rich data): full extraction with direct quotes

- **Non-tech role support**: Sales, marketing, operations, finance, HR — no more irrelevant Tech Stack or Code Review sections. Uses Universal dimensions (Workflow, Output Style, Knowledge Base).

- **Role auto-detection** from job title keywords when user doesn't specify category.

### ✨ UX Improvements (from Round 2)

- **One-shot creation**: Provide name + role + personality in one message → skip 3-question intake
- **Batch corrections**: Fix multiple persona issues in a single pass
- **Auto-apply simple corrections**: No confirmation needed (only on conflicts or Layer 0 changes)
- **Compact merger summaries**: Emoji + one-liner per file, auto-apply on zero conflicts
- **Honest "profile-only" markers**: No fictional examples when source data is skipped
- **Error Recovery**: Graceful script failures, off-script handling, interrupted creation resume
- **Full end-to-end demo** in README with one-shot creation → preview → live test

### 📁 New Files

| File | Purpose |
|------|---------|
| `prompts/smoke_test.md` | Post-creation quality validation protocol |
| `prompts/compare.md` | Side-by-side teammate comparison logic |
| `tools/privacy_guard.py` | PII scanner + auto-redactor |
| `tools/export.py` | Portable package export/import |

### 📊 Stats

- 30 files, ~5500 lines
- 9 prompt templates, 12 Python tools
- 8 language README versions

---

## [1.0.0] — 2026-03-31

Initial release.

- 3-question intake with one-shot mode
- Dual-track analysis (Work Skill + 5-layer Persona)
- 10 data source parsers (Slack, GitHub, Teams, Gmail, Notion, Confluence, JIRA, Linear, PDF, paste)
- Slack + GitHub auto-collectors
- Evolution mode (append files + conversation correction)
- Version management with rollback
- Dual-platform support (Claude Code + OpenClaw)
- 8-language README (EN, ZH, FR, DE, RU, JA, IT, ES)
- Example teammate: Alex Chen (Stripe L3 Backend)
