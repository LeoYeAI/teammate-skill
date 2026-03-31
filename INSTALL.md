# teammate.skill — Detailed Installation Guide

## Supported Platforms

| Platform | Type | Install Path |
|----------|------|-------------|
| [Claude Code](https://claude.ai/code) | Anthropic CLI | `.claude/skills/create-teammate` |
| [OpenClaw](https://openclaw.ai) 🦞 | Open-source personal AI (25+ channels, voice, canvas, cron) | `~/.openclaw/workspace/skills/create-teammate` |
| [MyClaw.ai](https://myclaw.ai) | Managed OpenClaw hosting (one-click, always-on) | Same as OpenClaw (pre-configured) |
| Other agents | Any AgentSkills-compatible agent | Your agent's skill directory |

---

## Quick Start (No Dependencies)

The simplest setup requires nothing — just install the skill and start creating teammates from manual descriptions.

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

Clone into your agent's skill directory. The skill follows the [AgentSkills](https://agentskills.io) standard — any compatible agent will auto-detect `SKILL.md`.

Then type `/create-teammate` in your agent.

---

## Optional: Data Source Integrations

### Slack Auto-Collector

Automatically pulls messages and threads from a Slack workspace.

**1. Create a Slack App**

Go to [api.slack.com/apps](https://api.slack.com/apps) → Create New App → From scratch.

**2. Add Bot Token Scopes**

Under "OAuth & Permissions", add:
- `channels:history` — read public channel messages
- `channels:read` — list channels
- `users:read` — resolve user names
- `groups:history` (optional) — read private channels
- `search:read` (optional) — search messages

**3. Install to Workspace**

Click "Install to Workspace" and authorize.

**4. Copy Bot Token**

Copy the `xoxb-...` token from "OAuth & Permissions".

**5. Configure**

```bash
python3 tools/slack_collector.py --setup
```

Paste your token when prompted. Config is saved to `~/.teammate-skill/slack_config.json`.

**6. Add Bot to Channels**

In Slack, add the bot to channels you want to collect from:
`/invite @YourBotName` in each channel.

**7. Collect**

```bash
python3 tools/slack_collector.py --username "alex.chen" --output-dir ./knowledge/alex
```

---

### GitHub Collector

Collects PRs, code reviews, and issue comments.

**1. Create a Personal Access Token**

Go to [github.com/settings/tokens](https://github.com/settings/tokens) → Generate new token (classic).

Scopes needed:
- `repo` (for private repos) or `public_repo` (for public only)

**2. Set Token**

```bash
export GITHUB_TOKEN="ghp_..."
```

Or pass directly:
```bash
python3 tools/github_collector.py --username "alexchen" --repos "stripe/payments-core" --token "ghp_..."
```

**3. Collect**

```bash
# From specific repos
python3 tools/github_collector.py --username "alexchen" --repos "org/repo1,org/repo2" --output-dir ./knowledge/alex

# From all repos in an org
python3 tools/github_collector.py --username "alexchen" --org "stripe" --output-dir ./knowledge/alex
```

---

### Gmail / Email

No setup needed — just export and parse.

**Export from Gmail:**
1. Go to [takeout.google.com](https://takeout.google.com)
2. Select only "Mail"
3. Download the `.mbox` file

**Parse:**
```bash
python3 tools/email_parser.py --file ~/Downloads/All\ mail.mbox --target "alex@company.com" --output ./knowledge/alex/emails.txt
```

---

### Microsoft Teams

**Export chat history:**
1. In Teams, open the chat/channel
2. Use the Teams admin export tool or compliance export
3. Save as JSON

**Parse:**
```bash
python3 tools/teams_parser.py --file teams_export.json --target "Alex Chen" --output ./knowledge/alex/teams.txt
```

---

### Notion

**Export from Notion:**
1. Go to Settings → Workspace → Export all workspace content
2. Choose "Markdown & CSV" or "HTML"
3. Download and unzip

**Parse:**
```bash
python3 tools/notion_parser.py --dir ~/Downloads/notion_export/ --target "Alex" --output ./knowledge/alex/notion.txt
```

---

### Confluence

**Export from Confluence:**
1. Space Settings → Export Space → HTML
2. Download the zip

**Parse:**
```bash
python3 tools/confluence_parser.py --file confluence_export.zip --target "Alex Chen" --output ./knowledge/alex/confluence.txt
```

---

### JIRA / Linear

**JIRA:** Filters → Export → CSV (all fields)
**Linear:** Settings → Export → JSON

```bash
# JIRA
python3 tools/project_tracker_parser.py --file jira_issues.csv --target "Alex Chen" --output ./knowledge/alex/jira.txt

# Linear
python3 tools/project_tracker_parser.py --file linear_export.json --target "alex" --output ./knowledge/alex/linear.txt
```

---

## Python Dependencies

Only needed if using auto-collectors:

```bash
pip3 install -r requirements.txt
```

Contents of `requirements.txt`:
- `slack_sdk>=3.0` — Slack API (for auto-collector only)
- No other hard dependencies — all parsers use Python stdlib

---

## Troubleshooting

### Slack: "not_in_channel" error
→ Add the bot to the channel: `/invite @YourBotName`

### Slack: "missing_scope" error
→ Add the required scope in your Slack App settings, then reinstall to workspace

### GitHub: "403 rate limit" error
→ Set `GITHUB_TOKEN` environment variable for authenticated requests (5000/hour vs 60/hour)

### Notion export is empty
→ Make sure you're exporting the workspace, not just a single page. Check that the target user has pages in the workspace.

### Parser finds 0 messages for target
→ Check the exact name/username. Use `--target` with the display name as it appears in the platform. The match is case-insensitive and partial.
