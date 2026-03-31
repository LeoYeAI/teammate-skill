<div align="center">

<h1><img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=50&duration=3000&pause=1000&color=6C63FF&center=true&vCenter=true&width=600&height=80&lines=teammate.skill" alt="teammate.skill" /></h1>

> *Your teammate left. Their context didn't have to.*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://python.org)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet)](https://claude.ai/code)
[![OpenClaw](https://img.shields.io/badge/🦞%20OpenClaw-Skill-orange)](https://github.com/openclaw/openclaw)
[![AgentSkills](https://img.shields.io/badge/AgentSkills-Standard-green)](https://agentskills.io)

[English](README.md) | [简体中文](README.zh-CN.md) | [Français](README.fr.md) | [Deutsch](README.de.md) | [Русский](README.ru.md) | [日本語](README.ja.md) | [Italiano](README.it.md) | [Español](README.es.md)

<br>

Your teammate quit and three years of tribal knowledge walked out the door.<br>
Your senior engineer left — no handoff doc, no runbook, just silence.<br>
Your co-founder pivoted, taking every unwritten decision with them.

**Feed in their Slack messages, GitHub PRs, emails, docs, and your own description —<br>
get an AI Skill that actually works like them.**

Writes code in their style. Reviews PRs with their standards. Answers questions in their voice.

<br>

[How It Works](#how-it-works) · [Install](#install) · [Data Sources](#supported-data-sources) · [Demo](#demo) · [Detailed Setup](INSTALL.md)

</div>

---

## How It Works

```
You describe your teammate (3 questions)
          ↓
Provide source materials (Slack, GitHub, email, docs — or skip)
          ↓
Dual-track AI analysis
  ├── Track A: Work Skill (systems, standards, workflows, review style)
  └── Track B: Persona (5-layer personality model)
          ↓
Generated SKILL.md — invoke anytime with /{slug}
          ↓
Evolve over time (append new data, correct mistakes, auto-version)
```

The generated skill has two parts that work together:

| Part | What it captures |
|------|-----------------|
| **Part A — Work Skill** | Systems owned · tech standards · code review focus · workflows · tribal knowledge |
| **Part B — Persona** | 5-layer model: hard rules → identity → expression → decision patterns → interpersonal style |

When invoked: **Persona decides the attitude → Work Skill executes → output in their voice**.

---

## Install

### 🦞 OpenClaw

**Option A — ClawHub (recommended):**
```bash
openclaw skills install create-teammate
```

**Option B — Git:**
```bash
git clone https://github.com/LeoYeAI/teammate-skill ~/.openclaw/workspace/skills/create-teammate
```

Then start a new session (`/new`) and type `/create-teammate`.

> **MyClaw.ai users**: Same as above — SSH into your instance or use the web terminal.

### Claude Code

```bash
# Per-project
mkdir -p .claude/skills
git clone https://github.com/LeoYeAI/teammate-skill .claude/skills/create-teammate

# Global (all projects)
git clone https://github.com/LeoYeAI/teammate-skill ~/.claude/skills/create-teammate
```

Then type `/create-teammate` in Claude Code.

### Other AgentSkills Agents

Clone into your agent's skill directory. Any agent that reads [AgentSkills](https://agentskills.io) `SKILL.md` frontmatter will auto-detect it.

### Optional Dependencies

```bash
pip3 install -r requirements.txt   # Only needed for Slack/GitHub auto-collectors
```

> Slack auto-collection needs a Bot Token. GitHub collection uses `GITHUB_TOKEN`. See [INSTALL.md](INSTALL.md) for setup guides.

---

## Supported Data Sources

| Source | Type | Method |
|--------|------|--------|
| **Slack** | Messages, threads, reactions | ✅ Auto-collect (enter username) or upload JSON export |
| **GitHub** | PRs, reviews, commits, issues | ✅ Auto-collect (enter handle) |
| **Gmail** | Emails | Upload `.mbox` / `.eml` from Google Takeout |
| **Teams / Outlook** | Chat, emails | Upload export JSON |
| **Notion** | Wiki, docs | Upload Markdown/HTML export |
| **Confluence** | Wiki, docs | Upload HTML export or zip |
| **JIRA / Linear** | Issues, tickets | Upload CSV / JSON export |
| **PDF / Images** | Any document | Upload directly |
| **Markdown / Text** | Anything | Upload or paste |

Mix and match any combination. Or skip entirely — even a one-sentence description generates a useful skill.

---

## Demo

> Example teammate: Stripe L3 backend engineer, INTJ, perfectionist, brutal code reviewer

**Code Review:**
```
You    ❯  Review this payment endpoint?

Alex   ❯  What problem does this solve? PR description doesn't say.
          
          Blocking: you're using float for amount. Use Decimal for financial
          values. Also this endpoint isn't idempotent — what happens on retry?
```

**Architecture Decision:**
```
You    ❯  Should we use MongoDB for this?

Alex   ❯  No. We need ACID for payment flows. Stick with Postgres.
          If the concern is schema flexibility, use JSONB columns.
```

**Pushback:**
```
You    ❯  Skip tests, ship by Friday?

Alex   ❯  No. Tests right or we don't ship. If Friday is hard,
          cut scope instead of cutting quality.
```

---

## Platform Compatibility

This skill is built to run natively on both platforms — no adapter layer, no workarounds.

| Feature | Claude Code | OpenClaw |
|---------|:-----------:|:--------:|
| Install | `.claude/skills/` | `openclaw skills install` or `~/.openclaw/workspace/skills/` |
| Trigger | `/create-teammate` | `/create-teammate` |
| Path resolution | `${CLAUDE_SKILL_DIR}` | `{baseDir}` (auto-resolved) |
| File operations | `Read` / `Write` / `Edit` | `read` / `write` / `edit` |
| Run scripts | `Bash` tool | `exec` tool |
| Fetch URLs | `Bash` → curl | `web_fetch` tool |
| Generated output | `./teammates/{slug}/` | `./teammates/{slug}/` |

The SKILL.md uses `{baseDir}` for all paths — both platforms resolve it automatically.

---

## Evolution

Teammate skills aren't static — they improve over time:

| Method | How |
|--------|-----|
| **Append data** | "I found more Slack logs" → auto-analyze delta, merge without overwriting |
| **Correct mistakes** | "They wouldn't say that, they'd say..." → instant correction |
| **Version control** | Every update auto-archives → rollback to any version |

---

## Commands

| Command | Description |
|---------|-------------|
| `/create-teammate` | Create a new teammate skill |
| `/list-teammates` | List all generated teammates |
| `/{slug}` | Invoke teammate (full persona + work) |
| `/{slug}-work` | Work capabilities only |
| `/{slug}-persona` | Persona only |
| `/update-teammate {slug}` | Add new materials to existing teammate |
| `/teammate-rollback {slug} {version}` | Rollback to previous version |
| `/delete-teammate {slug}` | Delete a teammate skill |

---

## Supported Tags

<details>
<summary><strong>Personality tags</strong> (click to expand)</summary>

Meticulous · Good-enough · Blame-deflector · Perfectionist · Procrastinator · Ship-fast · Over-engineer · Scope-creeper · Bike-shedder · Micro-manager · Hands-off · Devil's-advocate · Mentor-type · Gatekeeper · Passive-aggressive · Confrontational · Drama-free

</details>

<details>
<summary><strong>Corporate culture tags</strong></summary>

Google-style · Meta-style · Amazon-style · Apple-style · Stripe-style · Netflix-style · Microsoft-style · Startup-mode · Agency-mode · First-principles · Open-source-native

</details>

<details>
<summary><strong>Level mappings</strong></summary>

Google L3-L11 · Meta E3-E9 · Amazon L4-L10 · Stripe L1-L5 · Microsoft 59-67+ · Apple ICT2-ICT6 · Netflix · Uber · Airbnb · ByteDance · Alibaba · Tencent · Generic (Junior / Mid / Senior / Staff / Principal)

</details>

---

## Project Structure

```
create-teammate/
├── SKILL.md                      # Entry point (dual-platform)
├── prompts/                      # Prompt templates (loaded by SKILL.md)
│   ├── intake.md                 #   3-question info collection
│   ├── work_analyzer.md          #   Work capability extraction
│   ├── persona_analyzer.md       #   Personality extraction + tag translation
│   ├── work_builder.md           #   work.md generation
│   ├── persona_builder.md        #   persona.md 5-layer structure
│   ├── merger.md                 #   Incremental merge logic
│   └── correction_handler.md     #   Conversation correction
├── tools/                        # Python scripts (run via Bash/exec)
│   ├── slack_collector.py        #   Slack API auto-collector
│   ├── slack_parser.py           #   Slack export JSON parser
│   ├── github_collector.py       #   GitHub PR/review collector
│   ├── teams_parser.py           #   Teams/Outlook parser
│   ├── email_parser.py           #   Gmail .mbox/.eml parser
│   ├── notion_parser.py          #   Notion export parser
│   ├── confluence_parser.py      #   Confluence export parser
│   ├── project_tracker_parser.py #   JIRA/Linear parser
│   ├── skill_writer.py           #   Skill file management
│   └── version_manager.py        #   Version archive & rollback
├── teammates/                    # Generated teammate skills
│   └── example_alex/             #   Example: Stripe L3 backend engineer
├── requirements.txt
├── INSTALL.md                    # Detailed setup (API tokens, etc.)
└── LICENSE
```

---

## Best Practices

1. **Source quality = skill quality** — real chat logs and design docs beat manual descriptions
2. **Best sources by type**: design docs they wrote > code review comments > architecture discussions > casual chat
3. **GitHub PRs** are gold for Work Skill — they reveal actual coding standards
4. **Slack threads** are gold for Persona — they reveal communication style under pressure
5. **Start small** — create from description first, then append real data as you find it

---

## License

[MIT](LICENSE)

---

<div align="center">

**teammate.skill** — because the best knowledge transfer isn't a document, it's a working model.

<br>

Powered by [MyClaw.ai](https://myclaw.ai) · Built for [OpenClaw](https://github.com/openclaw/openclaw) & [Claude Code](https://claude.ai/code)

</div>
