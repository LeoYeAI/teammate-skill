<div align="center">

# teammate.skill

> *Your teammate left. Their context didn't have to.*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://python.org)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet)](https://claude.ai/code)
[![OpenClaw](https://img.shields.io/badge/OpenClaw-Skill-orange)](https://openclaw.ai)
[![AgentSkills](https://img.shields.io/badge/AgentSkills-Standard-green)](https://agentskills.io)

<br>

Your teammate quit, leaving behind a mountain of unmaintained docs?<br>
Your senior engineer left, taking all the tribal knowledge with them?<br>
Your mentor moved on, and three years of context vanished overnight?<br>
Your co-founder pivoted to a new role, and the handoff doc is two pages?<br>

**Turn departures into durable Skills. Welcome to knowledge immortality.**

<br>

Provide source materials (Slack messages, GitHub PRs, emails, Notion docs, meeting notes)<br>
plus your description of who they are<br>
and get an **AI Skill that actually works like them**<br>
— writes code in their style, reviews PRs with their standards, answers questions with their voice

[Supported Sources](#supported-data-sources) · [Install](#install) · [Usage](#usage) · [Demo](#demo) · [Detailed Install](INSTALL.md)

</div>

---

## Supported Data Sources

> Beta — more integrations coming soon!

| Source | Messages | Docs / Wiki | Code & PRs | Notes |
|--------|:--------:|:-----------:|:----------:|-------|
| Slack (auto-collect) | ✅ API | — | — | Enter username, fully automatic |
| GitHub (auto-collect) | — | — | ✅ API | PRs, reviews, issue comments |
| Slack export JSON | ✅ | — | — | Manual upload |
| Gmail `.mbox` / `.eml` | ✅ | — | — | Manual upload |
| Teams / Outlook export | ✅ | — | — | Manual upload |
| Notion export | — | ✅ | — | HTML or Markdown export |
| Confluence export | — | ✅ | — | HTML export or zip |
| JIRA CSV / Linear JSON | — | — | ✅ | Issue tracking exports |
| PDF | — | ✅ | — | Manual upload |
| Images / Screenshots | ✅ | — | — | Manual upload |
| Markdown / Text | ✅ | ✅ | — | Manual upload |
| Paste text directly | ✅ | — | — | Copy-paste anything |

---

## Platforms

### [Claude Code](https://claude.ai/code)
Anthropic's official CLI for Claude. Install this skill into `.claude/skills/` and invoke with `/create-teammate`.

### [OpenClaw](https://openclaw.ai) 🦞
Open-source personal AI assistant by [@steipete](https://github.com/steipete). Runs on your own devices, answers on 25+ channels (WhatsApp, Telegram, Slack, Discord, Teams, Signal, iMessage, and more). Local-first gateway, persistent memory, voice, canvas, cron jobs, and a growing skills ecosystem. [GitHub](https://github.com/openclaw/openclaw)

### [MyClaw.ai](https://myclaw.ai)
Managed hosting for OpenClaw — skip Docker, servers, and configs. One-click deploy, always-on, automatic updates, daily backups. Your OpenClaw instance live in minutes. Perfect if you want teammate.skill running 24/7 without self-hosting.

---

## Install

This skill follows the [AgentSkills](https://agentskills.io) open standard and works with any compatible agent.

### Claude Code

```bash
# Per-project (at git repo root)
mkdir -p .claude/skills
git clone https://github.com/LeoYeAI/teammate-skill .claude/skills/create-teammate

# Global (all projects)
git clone https://github.com/LeoYeAI/teammate-skill ~/.claude/skills/create-teammate
```

### OpenClaw

```bash
git clone https://github.com/LeoYeAI/teammate-skill ~/.openclaw/workspace/skills/create-teammate
```

### Other AgentSkills-Compatible Agents

Clone into your agent's skill directory. The entry point is `SKILL.md` with standard frontmatter — any agent that reads AgentSkills format will pick it up automatically.

### Dependencies (optional)

```bash
pip3 install -r requirements.txt
```

> Slack auto-collection requires a Bot Token. GitHub collection uses `GITHUB_TOKEN`. See [INSTALL.md](INSTALL.md).

---

## Usage

In your agent (Claude Code, OpenClaw, or any AgentSkills-compatible agent), type:

```
/create-teammate
```

Follow the prompts: enter a name, role info (e.g. `Google L5 backend engineer`), personality tags, then choose data sources. Everything except the name is skippable — even a description alone generates a useful Skill.

Once created, invoke the teammate with `/{slug}`.

### Commands

| Command | Description |
|---------|-------------|
| `/create-teammate` | Create a new teammate Skill |
| `/list-teammates` | List all teammate Skills |
| `/{slug}` | Invoke full Skill (Persona + Work) |
| `/{slug}-work` | Work capabilities only |
| `/{slug}-persona` | Persona only |
| `/teammate-rollback {slug} {version}` | Rollback to a previous version |
| `/delete-teammate {slug}` | Delete a teammate Skill |

---

## Demo

> Input: `Stripe L3 backend engineer, INTJ, perfectionist, Stripe-style, brutal code reviewer`

**Scenario 1: Code Review**

```
User              ❯ Can you review this API endpoint?

teammate.skill    ❯ What problem does this actually solve? The PR description
                    doesn't say. Adding that first.
                    
                    Looking at the code: you're using float for the amount
                    field. That's a blocking issue — use Decimal for financial
                    values. Also, this endpoint isn't idempotent. What happens
                    on retry?
```

**Scenario 2: Design Discussion**

```
User              ❯ Should we use MongoDB for this new feature?

teammate.skill    ❯ Strong disagree. We need ACID transactions for payment
                    flows. Mongo doesn't give us that. Let's stick with
                    Postgres. If the concern is schema flexibility, we can
                    use JSONB columns.
```

**Scenario 3: Pushback**

```
User              ❯ Can we skip tests and ship this by Friday?

teammate.skill    ❯ No. We get the tests right or we don't ship. If Friday
                    is a hard deadline, let's cut scope instead of cutting
                    quality. What's the minimum we need for launch?
```

---

## Features

### Generated Skill Structure

Each teammate Skill has two parts that work together:

| Part | Content |
|------|---------|
| **Part A — Work Skill** | Systems owned, tech standards, workflows, CR focus, experience |
| **Part B — Persona** | 5-layer personality: hard rules → identity → expression → decisions → interpersonal |

Execution: `Receive task → Persona decides attitude → Work Skill executes → Output in their voice`

### Supported Tags

**Personality**: Meticulous · Good-enough · Blame-deflector · Perfectionist · Procrastinator · Ship-fast · Over-engineer · Scope-creeper · Bike-shedder · Micro-manager · Hands-off · Devil's-advocate · Mentor-type · Gatekeeper · Passive-aggressive · Confrontational …

**Corporate culture**: Google-style · Meta-style · Amazon-style · Apple-style · Stripe-style · Netflix-style · Microsoft-style · Startup-mode · Agency-mode · First-principles · Open-source-native

**Levels**: Google L3-L11 · Meta E3-E9 · Amazon L4-L10 · Stripe L1-L5 · Microsoft 59-67+ · Apple ICT2-ICT6 · Netflix · Uber · Airbnb · ByteDance · Alibaba · Tencent · Generic (Junior/Senior/Staff/Principal)

### Evolution

- **Append files** → auto-analyze delta → merge into relevant sections, never overwrite existing conclusions
- **Conversation correction** → say "they wouldn't do that, they would..." → writes to Correction layer, takes effect immediately
- **Version control** → auto-archive on every update, rollback to any previous version

---

## Project Structure

This project follows the [AgentSkills](https://agentskills.io) open standard:

```
create-teammate/
├── SKILL.md                  # Skill entry point
├── prompts/                  # Prompt templates
│   ├── intake.md             #   Info collection (3 questions)
│   ├── work_analyzer.md      #   Work capability extraction
│   ├── persona_analyzer.md   #   Personality extraction + tag translation
│   ├── work_builder.md       #   work.md generation template
│   ├── persona_builder.md    #   persona.md 5-layer structure
│   ├── merger.md             #   Incremental merge logic
│   └── correction_handler.md #   Conversation correction handler
├── tools/                    # Data collection & management
│   ├── slack_collector.py    #   Slack auto-collector (Bot Token)
│   ├── slack_parser.py       #   Slack export JSON parser
│   ├── github_collector.py   #   GitHub PR/review collector
│   ├── teams_parser.py       #   Teams/Outlook parser
│   ├── email_parser.py       #   Gmail .mbox/.eml parser
│   ├── notion_parser.py      #   Notion export parser
│   ├── confluence_parser.py  #   Confluence export parser
│   ├── project_tracker_parser.py # JIRA/Linear parser
│   ├── skill_writer.py       #   Skill file management
│   └── version_manager.py    #   Version archive & rollback
├── teammates/                # Generated teammate Skills
│   └── example_alex/         #   Example: Stripe L3 backend engineer
├── docs/
├── requirements.txt
├── INSTALL.md
└── LICENSE
```

---

## Best Practices

- **Source material quality = Skill quality**: real chat logs + design docs > manual description only
- Prioritize collecting: **design docs they authored** > **code review comments** > **decision discussions** > casual chat
- GitHub PRs and reviews are goldmines for Work Skill — they reveal actual coding standards and review priorities
- Slack threads are goldmines for Persona — they reveal communication style under different pressures
- Start with manual description, then append real data incrementally as you find it

---

## License

MIT License — see [LICENSE](LICENSE) for details.

---

<div align="center">

**teammate.skill** — because the best knowledge transfer isn't a document, it's a working model.

</div>
