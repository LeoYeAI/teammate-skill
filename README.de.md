[English](README.md) | [简体中文](README.zh-CN.md) | [Français](README.fr.md) | [Deutsch](README.de.md) | [Русский](README.ru.md) | [日本語](README.ja.md) | [Italiano](README.it.md) | [Español](README.es.md)

<div align="center">

<h1><img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=50&duration=3000&pause=1000&color=6C63FF&center=true&vCenter=true&width=600&height=80&lines=teammate.skill" alt="teammate.skill" /></h1>

> *Dein Teamkollege ist gegangen. Sein Kontext musste es nicht.*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://python.org)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet)](https://claude.ai/code)
[![OpenClaw](https://img.shields.io/badge/OpenClaw-Skill-orange)](https://openclaw.ai)
[![AgentSkills](https://img.shields.io/badge/AgentSkills-Standard-green)](https://agentskills.io)

<br>

Dein Teamkollege hat gekündigt und einen Berg ungepflegter Dokumentation hinterlassen?<br>
Dein Senior-Engineer ist gegangen und hat das gesamte Stammwissen mitgenommen?<br>
Dein Mentor hat gewechselt, und drei Jahre Kontext sind über Nacht verschwunden?<br>
Dein Mitgründer hat die Rolle gewechselt, und das Übergabedokument ist zwei Seiten lang?<br>

**Verwandle Abgänge in dauerhafte Skills. Willkommen zur Unsterblichkeit des Wissens.**

<br>

Stelle Quellmaterialien bereit (Slack-Nachrichten, GitHub-PRs, E-Mails, Notion-Docs, Meeting-Notizen)<br>
plus deine Beschreibung, wer sie sind<br>
und erhalte einen **KI-Skill, der wirklich wie sie arbeitet**<br>
— schreibt Code in ihrem Stil, reviewt PRs nach ihren Standards, beantwortet Fragen mit ihrer Stimme

[Unterstützte Quellen](#unterstützte-datenquellen) · [Installation](#installation) · [Nutzung](#nutzung) · [Demo](#demo) · [Detaillierte Installation](INSTALL.md)

</div>

---

## Unterstützte Datenquellen

> Beta — weitere Integrationen folgen bald!

| Quelle | Nachrichten | Docs / Wiki | Code & PRs | Hinweise |
|--------|:-----------:|:-----------:|:----------:|----------|
| Slack (automatische Erfassung) | ✅ API | — | — | Benutzernamen eingeben, vollautomatisch |
| GitHub (automatische Erfassung) | — | — | ✅ API | PRs, Reviews, Issue-Kommentare |
| Slack-Export JSON | ✅ | — | — | Manueller Upload |
| Gmail `.mbox` / `.eml` | ✅ | — | — | Manueller Upload |
| Teams / Outlook-Export | ✅ | — | — | Manueller Upload |
| Notion-Export | — | ✅ | — | HTML- oder Markdown-Export |
| Confluence-Export | — | ✅ | — | HTML-Export oder Zip |
| JIRA CSV / Linear JSON | — | — | ✅ | Projektmanagement-Exporte |
| PDF | — | ✅ | — | Manueller Upload |
| Bilder / Screenshots | ✅ | — | — | Manueller Upload |
| Markdown / Text | ✅ | ✅ | — | Manueller Upload |
| Text direkt einfügen | ✅ | — | — | Beliebigen Text kopieren & einfügen |

---

## Plattformen

### [Claude Code](https://claude.ai/code)
Anthropics offizielles CLI für Claude. Installiere diesen Skill in `.claude/skills/` und rufe ihn mit `/create-teammate` auf.

### [OpenClaw](https://openclaw.ai) 🦞
Open-Source persönlicher KI-Assistent von [@steipete](https://github.com/steipete). Läuft auf deinen eigenen Geräten, antwortet über 25+ Kanäle (WhatsApp, Telegram, Slack, Discord, Teams, Signal, iMessage und mehr). Local-first Gateway, persistenter Speicher, Sprache, Canvas, Cronjobs und ein wachsendes Skill-Ökosystem. [GitHub](https://github.com/openclaw/openclaw)

### 🏆 [MyClaw.ai](https://myclaw.ai)
Managed Hosting für OpenClaw — vergiss Docker, Server und Konfigurationen. Ein-Klick-Deployment, immer online, automatische Updates, tägliche Backups. Deine OpenClaw-Instanz in wenigen Minuten live. Perfekt, wenn du teammate.skill rund um die Uhr laufen lassen willst, ohne selbst zu hosten.

---

## Installation

Dieser Skill folgt dem offenen [AgentSkills](https://agentskills.io)-Standard und funktioniert mit jedem kompatiblen Agenten.

### Claude Code

```bash
# Pro Projekt (im Git-Repository-Root)
mkdir -p .claude/skills
git clone https://github.com/LeoYeAI/teammate-skill .claude/skills/create-teammate

# Global (alle Projekte)
git clone https://github.com/LeoYeAI/teammate-skill ~/.claude/skills/create-teammate
```

### OpenClaw

```bash
git clone https://github.com/LeoYeAI/teammate-skill ~/.openclaw/workspace/skills/create-teammate
```

### Andere AgentSkills-kompatible Agenten

Klone in das Skill-Verzeichnis deines Agenten. Der Einstiegspunkt ist `SKILL.md` mit Standard-Frontmatter — jeder Agent, der das AgentSkills-Format unterstützt, erkennt ihn automatisch.

### Abhängigkeiten (optional)

```bash
pip3 install -r requirements.txt
```

> Die automatische Slack-Erfassung erfordert ein Bot Token. Die GitHub-Erfassung nutzt `GITHUB_TOKEN`. Siehe [INSTALL.md](INSTALL.md).

---

## Nutzung

Gib in deinem Agenten (Claude Code, OpenClaw oder jedem AgentSkills-kompatiblen Agenten) ein:

```
/create-teammate
```

Folge den Anweisungen: gib einen Namen ein, Rolleninformationen (z.B. `Google L5 backend engineer`), Persönlichkeits-Tags, dann wähle die Datenquellen. Alles außer dem Namen kann übersprungen werden — selbst eine reine Beschreibung erzeugt einen nützlichen Skill.

Nach der Erstellung rufst du den Teamkollegen mit `/{slug}` auf.

### Befehle

| Befehl | Beschreibung |
|--------|-------------|
| `/create-teammate` | Neuen Teamkollegen-Skill erstellen |
| `/list-teammates` | Alle Teamkollegen-Skills auflisten |
| `/{slug}` | Vollständigen Skill aufrufen (Persona + Arbeit) |
| `/{slug}-work` | Nur Arbeitsfähigkeiten |
| `/{slug}-persona` | Nur Persona |
| `/compare {a} vs {b}` | Vergleich nebeneinander mit Szenario-Simulation |
| `/export-teammate {slug}` | Portables `.tar.gz`-Paket zum Teilen exportieren |
| `/update-teammate {slug}` | Neue Materialien zu bestehendem Teamkollegen hinzufügen |
| `/teammate-rollback {slug} {version}` | Auf eine frühere Version zurückrollen |
| `/delete-teammate {slug}` | Einen Teamkollegen-Skill löschen |

---

## Demo

> Eingabe: `Stripe L3 backend engineer, INTJ, perfectionist, Stripe-style, brutal code reviewer`

**Szenario 1: Code-Review**

```
User              ❯ Can you review this API endpoint?

teammate.skill    ❯ What problem does this actually solve? The PR description
                    doesn't say. Adding that first.
                    
                    Looking at the code: you're using float for the amount
                    field. That's a blocking issue — use Decimal for financial
                    values. Also, this endpoint isn't idempotent. What happens
                    on retry?
```

**Szenario 2: Design-Diskussion**

```
User              ❯ Should we use MongoDB for this new feature?

teammate.skill    ❯ Strong disagree. We need ACID transactions for payment
                    flows. Mongo doesn't give us that. Let's stick with
                    Postgres. If the concern is schema flexibility, we can
                    use JSONB columns.
```

**Szenario 3: Widerstand**

```
User              ❯ Can we skip tests and ship this by Friday?

teammate.skill    ❯ No. We get the tests right or we don't ship. If Friday
                    is a hard deadline, let's cut scope instead of cutting
                    quality. What's the minimum we need for launch?
```

---

## Funktionen

### Generierte Skill-Struktur

Jeder Teamkollegen-Skill besteht aus zwei zusammenwirkenden Teilen:

| Teil | Inhalt |
|------|--------|
| **Part A — Arbeitsfähigkeiten** | Verwaltete Systeme, technische Standards, Workflows, CR-Fokus, Erfahrung |
| **Part B — Persona** | 5-schichtige Persönlichkeit: harte Regeln → Identität → Ausdruck → Entscheidungen → Zwischenmenschliches |

Ausführung: `Aufgabe empfangen → Persona bestimmt Haltung → Arbeitsfähigkeiten führen aus → Ausgabe in ihrer Stimme`

### Unterstützte Tags

**Persönlichkeit**: Meticulous · Good-enough · Blame-deflector · Perfectionist · Procrastinator · Ship-fast · Over-engineer · Scope-creeper · Bike-shedder · Micro-manager · Hands-off · Devil's-advocate · Mentor-type · Gatekeeper · Passive-aggressive · Confrontational …

**Unternehmenskultur**: Google-style · Meta-style · Amazon-style · Apple-style · Stripe-style · Netflix-style · Microsoft-style · Startup-mode · Agency-mode · First-principles · Open-source-native

**Level**: Google L3-L11 · Meta E3-E9 · Amazon L4-L10 · Stripe L1-L5 · Microsoft 59-67+ · Apple ICT2-ICT6 · Netflix · Uber · Airbnb · ByteDance · Alibaba · Tencent · Generic (Junior/Senior/Staff/Principal)

### Evolution

- **Dateien hinzufügen** → automatische Delta-Analyse → Zusammenführung in relevante Abschnitte, bestehende Schlussfolgerungen werden nie überschrieben
- **Gesprächskorrektur** → sage „Das würden sie nicht tun, sie würden..." → schreibt in die Korrekturschicht, wirkt sofort
- **Versionskontrolle** → automatische Archivierung bei jedem Update, Rollback auf jede beliebige Version

---

## Qualitätssicherung

Jeder Teamkollege durchläuft eine **3-stufige Qualitätspipeline** bevor du ihn erhältst:

### 1. Quality Gate (vor der Vorschau)
Validiert generierten Inhalt anhand von 7 strengen Regeln: Layer 0-Konkretheit, Anzahl der Beispiele, Dichte der Redewendungen, Prioritätsreihenfolge, Bereichsdefinition, kein generischer Fülltext, Tag→Regel-Vollständigkeit. Fehler werden automatisch korrigiert, bevor du die Vorschau siehst.

### 2. Smoke Test (nach der Erstellung)
Drei automatisierte Test-Prompts werden gegen jeden generierten Skill ausgeführt:
- **Domänenfrage** — nutzt der Skill echte Systeme/Tools statt generischer Ratschläge?
- **Druckszenario** — hält die Persona unter Druck stand oder fällt sie in generische KI zurück?
- **Frage außerhalb des Bereichs** — gibt der Skill Wissensgrenzen im Charakter zu?

```
🧪 Smoke Test: ✅ Domain ✅ Pushback ✅ Out-of-scope — 3/3 passed
```

### 3. Datenschutz-Scan (vor dem Export)
Automatische Erkennung von E-Mails, Telefonnummern, API-Tokens, Sozialversicherungsnummern und anderen personenbezogenen Daten:
```bash
python3 tools/privacy_guard.py --scan teammates/alex-chen/          # erkennen
python3 tools/privacy_guard.py --scan teammates/alex-chen/ --redact  # automatisch bereinigen
```

Rohe Wissensdateien (`knowledge/`) werden standardmäßig von Git und Exporten ausgeschlossen.

---

## Teamkollegen vergleichen

Vergleich nebeneinander mit Szenario-Simulation:

```
You    ❯  /compare alex-chen vs bob-smith

Agent  ❯  ━━━ alex-chen vs bob-smith ━━━
                         alex-chen              bob-smith
          Priority:      Correctness > Speed    Ship fast > Perfect
          CR Style:      Blocking on naming     Suggestions only
          Under Pressure: Gets quieter           Gets louder
          Says "No" by:  Direct refusal          Asking questions

You    ❯  Who should review the payments API redesign?

Agent  ❯  alex-chen: "Send me the design doc. I want to check
             idempotency and error contracts."
          bob-smith: "Let's hop on a call and walk through it."

          Recommendation: alex-chen for correctness rigor.
```

Unterstützt auch **Entscheidungssimulation** — beobachte, wie zwei Teamkollegen im Charakter über eine technische Entscheidung debattieren.

---

## Exportieren & Teilen

Teamkollegen als portable Pakete exportieren:

```bash
/export-teammate alex-chen
# → alex-chen.teammate.tar.gz (nur Skill-Dateien, keine Rohdaten)

# Auf einer anderen Maschine importieren:
tar xzf alex-chen.teammate.tar.gz -C ./teammates/
```

Der Export enthält: SKILL.md, work.md, persona.md, meta.json, Versionshistorie und ein Manifest.
Rohe Wissensdateien sind standardmäßig ausgeschlossen — füge `--include-knowledge` hinzu, falls nötig (⚠️ enthält personenbezogene Daten).

---

## Projektstruktur

Dieses Projekt folgt dem offenen [AgentSkills](https://agentskills.io)-Standard:

```
create-teammate/
├── SKILL.md                  # Skill-Einstiegspunkt
├── prompts/                  # Prompt-Vorlagen
│   ├── intake.md             #   Informationserfassung (3 Fragen)
│   ├── work_analyzer.md      #   Extraktion der Arbeitsfähigkeiten
│   ├── persona_analyzer.md   #   Persönlichkeitsextraktion + Tag-Übersetzung
│   ├── work_builder.md       #   work.md Generierungsvorlage
│   ├── persona_builder.md    #   persona.md 5-Schichten-Struktur
│   ├── merger.md             #   Inkrementelle Zusammenführungslogik
│   ├── correction_handler.md #   Gesprächskorrektur-Handler
│   ├── compare.md            #   Teamkollegen-Vergleich nebeneinander
│   └── smoke_test.md         #   Qualitätsvalidierung nach Erstellung
├── tools/                    # Datenerfassung & Verwaltung
│   ├── slack_collector.py    #   Slack Auto-Collector (Bot Token)
│   ├── slack_parser.py       #   Slack-Export JSON-Parser
│   ├── github_collector.py   #   GitHub PR/Review-Collector
│   ├── teams_parser.py       #   Teams/Outlook-Parser
│   ├── email_parser.py       #   Gmail .mbox/.eml-Parser
│   ├── notion_parser.py      #   Notion-Export-Parser
│   ├── confluence_parser.py  #   Confluence-Export-Parser
│   ├── project_tracker_parser.py # JIRA/Linear-Parser
│   ├── skill_writer.py       #   Skill-Dateiverwaltung
│   ├── version_manager.py    #   Versionsarchivierung & Rollback
│   ├── privacy_guard.py      #   PII-Scanner & Auto-Schwärzung
│   └── export.py             #   Portabler Paket-Export/Import
├── teammates/                # Generierte Teamkollegen-Skills
│   └── example_alex/         #   Beispiel: Stripe L3 Backend-Engineer
├── docs/
├── requirements.txt
├── INSTALL.md
└── LICENSE
```

---

## Best Practices

- **Qualität der Quellmaterialien = Qualität des Skills**: echte Chat-Protokolle + Design-Docs > reine manuelle Beschreibung
- Priorisiere die Erfassung von: **Design-Docs, die sie verfasst haben** > **Code-Review-Kommentare** > **Entscheidungsdiskussionen** > lockerer Chat
- GitHub-PRs und Reviews sind Goldgruben für Arbeitsfähigkeiten — sie enthüllen tatsächliche Codierstandards und Review-Prioritäten
- Slack-Threads sind Goldgruben für die Persona — sie zeigen den Kommunikationsstil unter verschiedenen Drucksituationen
- Beginne mit einer manuellen Beschreibung, dann füge schrittweise echte Daten hinzu, sobald du sie findest

---

## Lizenz

MIT License — siehe [LICENSE](LICENSE) für Details.

---

<div align="center">

**teammate.skill** — weil der beste Wissenstransfer kein Dokument ist, sondern ein funktionierendes Modell.

</div>
