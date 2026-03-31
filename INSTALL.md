# teammate.skill — Installation & Setup Guide

## Quick Start (30 seconds, no dependencies)

### 🦞 OpenClaw

```bash
# Option A: ClawHub (recommended)
openclaw skills install create-teammate

# Option B: Git
git clone https://github.com/LeoYeAI/teammate-skill ~/.openclaw/workspace/skills/create-teammate
```

Start a new session (`/new`), then type `/create-teammate`.

> **MyClaw.ai users**: SSH into your instance or use the web terminal. Same commands.

### Claude Code

```bash
# Per-project (at your git repo root)
mkdir -p .claude/skills
git clone https://github.com/LeoYeAI/teammate-skill .claude/skills/create-teammate

# Or global (all projects)
git clone https://github.com/LeoYeAI/teammate-skill ~/.claude/skills/create-teammate
```

Then type `/create-teammate`.

### Other AgentSkills Agents

Clone into your agent's skill directory. The entry point is `SKILL.md` with standard [AgentSkills](https://agentskills.io) frontmatter.

---

## Verify Installation

**OpenClaw:**
```bash
openclaw skills list          # Should show "create-teammate"
```

**Claude Code:**
```bash
# In Claude Code, type:
/create-teammate              # Should trigger the skill
```

---

## Optional: Auto-Collector Setup

The basic skill works with zero dependencies — you can create teammates from descriptions and manually uploaded files. The auto-collectors below are optional power features.

### Python Dependencies

```bash
pip3 install -r requirements.txt
```

This installs `slack_sdk>=3.0`. All other parsers use Python stdlib only.

---

### Slack Auto-Collector

Pulls messages, threads, and reactions automatically via API.

**Step 1: Create a Slack App**

1. Go to [api.slack.com/apps](https://api.slack.com/apps) → **Create New App** → From scratch
2. Name it anything (e.g. "Teammate Collector")
3. Select your workspace

**Step 2: Add Bot Token Scopes**

Go to **OAuth & Permissions** → **Bot Token Scopes** and add:

| Scope | Purpose |
|-------|---------|
| `channels:history` | Read public channel messages |
| `channels:read` | List channels |
| `users:read` | Resolve usernames to display names |
| `groups:history` | *(optional)* Read private channels |
| `search:read` | *(optional)* Search messages |

**Step 3: Install & Copy Token**

1. Click **Install to Workspace** → Authorize
2. Copy the **Bot User OAuth Token** (`xoxb-...`)

**Step 4: Configure**

```bash
python3 tools/slack_collector.py --setup
# Paste your xoxb-... token when prompted
# Config saved to ~/.teammate-skill/slack_config.json
```

**Step 5: Add Bot to Channels**

In Slack, invite the bot to channels you want to collect from:
```
/invite @YourBotName
```

**Step 6: Collect**

```bash
python3 tools/slack_collector.py \
  --username "alex.chen" \
  --output-dir ./knowledge/alex-chen \
  --msg-limit 1000 \
  --channel-limit 20
```

Output files:
- `knowledge/alex-chen/messages.txt` — all messages
- `knowledge/alex-chen/threads.txt` — thread conversations
- `knowledge/alex-chen/collection_summary.json` — stats

---

### GitHub Collector

Pulls PRs, code reviews, commit messages, and issue comments.

**Step 1: Create a Personal Access Token**

1. Go to [github.com/settings/tokens](https://github.com/settings/tokens) → **Generate new token (classic)**
2. Select scope: `repo` (private repos) or `public_repo` (public only)

**Step 2: Set Token**

```bash
export GITHUB_TOKEN="ghp_..."
```

**Step 3: Collect**

```bash
# Specific repos
python3 tools/github_collector.py \
  --username "alexchen" \
  --repos "stripe/payments-core,stripe/api-gateway" \
  --output-dir ./knowledge/alex-chen \
  --pr-limit 50 \
  --review-limit 100

# All repos in an org
python3 tools/github_collector.py \
  --username "alexchen" \
  --org "stripe" \
  --output-dir ./knowledge/alex-chen
```

Output files:
- `knowledge/alex-chen/prs.txt` — PR descriptions + commits
- `knowledge/alex-chen/reviews.txt` — code review comments
- `knowledge/alex-chen/issues.txt` — issue activity

---

### Gmail / Email

No API setup needed — just export and parse.

**Export:**
1. [takeout.google.com](https://takeout.google.com) → select **Mail** only → download `.mbox`

**Parse:**
```bash
python3 tools/email_parser.py \
  --file ~/Downloads/All\ mail.mbox \
  --target "alex@company.com" \
  --output ./knowledge/alex-chen/emails.txt
```

---

### Microsoft Teams

**Export** via Teams admin or compliance export → save as JSON.

```bash
python3 tools/teams_parser.py \
  --file teams_export.json \
  --target "Alex Chen" \
  --output ./knowledge/alex-chen/teams.txt
```

---

### Notion

**Export:** Settings → Workspace → Export → Markdown & CSV or HTML → unzip.

```bash
python3 tools/notion_parser.py \
  --dir ~/Downloads/notion_export/ \
  --target "Alex" \
  --output ./knowledge/alex-chen/notion.txt
```

---

### Confluence

**Export:** Space Settings → Export Space → HTML → download zip.

```bash
python3 tools/confluence_parser.py \
  --file confluence_export.zip \
  --target "Alex Chen" \
  --output ./knowledge/alex-chen/confluence.txt
```

---

### JIRA / Linear

**JIRA:** Filters → Export → CSV (all fields)
**Linear:** Settings → Export → JSON

```bash
# JIRA
python3 tools/project_tracker_parser.py \
  --file jira_issues.csv \
  --target "Alex Chen" \
  --output ./knowledge/alex-chen/jira.txt

# Linear
python3 tools/project_tracker_parser.py \
  --file linear_export.json \
  --target "alex" \
  --output ./knowledge/alex-chen/linear.txt
```

---

## Troubleshooting

| Error | Fix |
|-------|-----|
| Slack: `not_in_channel` | `/invite @YourBotName` in the channel |
| Slack: `missing_scope` | Add scope in Slack App settings → reinstall to workspace |
| GitHub: `403 rate limit` | Set `GITHUB_TOKEN` (5000 req/hr vs 60/hr unauthenticated) |
| Notion export empty | Export full workspace, not single page |
| Parser finds 0 messages | Check `--target` name — match is case-insensitive and partial |
| OpenClaw: skill not showing | Run `/new` to start a fresh session, or `openclaw gateway restart` |
| Claude Code: skill not triggering | Verify skill is in `.claude/skills/` and directory contains `SKILL.md` |

---

## Updating

```bash
# OpenClaw (ClawHub)
openclaw skills update create-teammate

# Git install (both platforms)
cd <your-skill-directory>/create-teammate
git pull
```

Start a new session after updating to pick up changes.
