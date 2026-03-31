[English](README.md) | [简体中文](README.zh-CN.md) | [Français](README.fr.md) | [Deutsch](README.de.md) | [Русский](README.ru.md) | [日本語](README.ja.md) | [Italiano](README.it.md) | [Español](README.es.md)

<div align="center">

<h1><img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=50&duration=3000&pause=1000&color=6C63FF&center=true&vCenter=true&width=600&height=80&lines=teammate.skill" alt="teammate.skill" /></h1>

> *Votre collègue est parti. Son contexte n'avait pas à disparaître.*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://python.org)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet)](https://claude.ai/code)
[![OpenClaw](https://img.shields.io/badge/OpenClaw-Skill-orange)](https://openclaw.ai)
[![AgentSkills](https://img.shields.io/badge/AgentSkills-Standard-green)](https://agentskills.io)

<br>

Votre collègue a démissionné, laissant derrière lui une montagne de docs non maintenues ?<br>
Votre ingénieur senior est parti, emportant tout le savoir tribal avec lui ?<br>
Votre mentor a quitté l'équipe, et trois ans de contexte se sont évaporés du jour au lendemain ?<br>
Votre co-fondateur a changé de poste, et le document de passation fait deux pages ?<br>

**Transformez les départs en Skills durables. Bienvenue dans l'ère de l'immortalité du savoir.**

<br>

Fournissez des matériaux source (messages Slack, PRs GitHub, e-mails, docs Notion, notes de réunion)<br>
plus votre description de qui ils sont<br>
et obtenez un **Skill IA qui fonctionne vraiment comme eux**<br>
— écrit du code dans leur style, review les PRs selon leurs standards, répond aux questions avec leur voix

[Sources supportées](#sources-de-données-supportées) · [Installation](#installation) · [Utilisation](#utilisation) · [Démo](#démo) · [Installation détaillée](INSTALL.md)

</div>

---

## Sources de données supportées

> Beta — d'autres intégrations arrivent bientôt !

| Source | Messages | Docs / Wiki | Code & PRs | Notes |
|--------|:--------:|:-----------:|:----------:|-------|
| Slack (collecte auto) | ✅ API | — | — | Entrez le nom d'utilisateur, entièrement automatique |
| GitHub (collecte auto) | — | — | ✅ API | PRs, reviews, commentaires d'issues |
| Slack export JSON | ✅ | — | — | Upload manuel |
| Gmail `.mbox` / `.eml` | ✅ | — | — | Upload manuel |
| Teams / Outlook export | ✅ | — | — | Upload manuel |
| Notion export | — | ✅ | — | Export HTML ou Markdown |
| Confluence export | — | ✅ | — | Export HTML ou zip |
| JIRA CSV / Linear JSON | — | — | ✅ | Exports de suivi de projets |
| PDF | — | ✅ | — | Upload manuel |
| Images / Captures d'écran | ✅ | — | — | Upload manuel |
| Markdown / Text | ✅ | ✅ | — | Upload manuel |
| Coller du texte directement | ✅ | — | — | Copier-coller n'importe quoi |

---

## Plateformes

### [Claude Code](https://claude.ai/code)
Le CLI officiel d'Anthropic pour Claude. Installez ce Skill dans `.claude/skills/` et invoquez-le avec `/create-teammate`.

### [OpenClaw](https://openclaw.ai) 🦞
Assistant IA personnel open-source par [@steipete](https://github.com/steipete). Fonctionne sur vos propres appareils, répond sur plus de 25 canaux (WhatsApp, Telegram, Slack, Discord, Teams, Signal, iMessage, et plus). Gateway local-first, mémoire persistante, voix, canvas, tâches planifiées, et un écosystème de Skills en pleine croissance. [GitHub](https://github.com/openclaw/openclaw)

### 🏆 [MyClaw.ai](https://myclaw.ai)
Hébergement managé pour OpenClaw — oubliez Docker, les serveurs et les configs. Déploiement en un clic, toujours en ligne, mises à jour automatiques, sauvegardes quotidiennes. Votre instance OpenClaw en quelques minutes. Parfait si vous voulez faire tourner teammate.skill 24h/24 sans auto-hébergement.

---

## Installation

Ce Skill suit le standard ouvert [AgentSkills](https://agentskills.io) et fonctionne avec tout agent compatible.

### Claude Code

```bash
# Par projet (à la racine du dépôt git)
mkdir -p .claude/skills
git clone https://github.com/LeoYeAI/teammate-skill .claude/skills/create-teammate

# Global (tous les projets)
git clone https://github.com/LeoYeAI/teammate-skill ~/.claude/skills/create-teammate
```

### OpenClaw

```bash
git clone https://github.com/LeoYeAI/teammate-skill ~/.openclaw/workspace/skills/create-teammate
```

### Autres agents compatibles AgentSkills

Clonez dans le répertoire de Skills de votre agent. Le point d'entrée est `SKILL.md` avec un frontmatter standard — tout agent supportant le format AgentSkills le détectera automatiquement.

### Dépendances (optionnel)

```bash
pip3 install -r requirements.txt
```

> La collecte automatique Slack nécessite un Bot Token. La collecte GitHub utilise `GITHUB_TOKEN`. Voir [INSTALL.md](INSTALL.md).

---

## Utilisation

Dans votre agent (Claude Code, OpenClaw, ou tout agent compatible AgentSkills), tapez :

```
/create-teammate
```

Suivez les instructions : entrez un nom, des infos sur le rôle (ex. `Google L5 backend engineer`), des tags de personnalité, puis choisissez les sources de données. Tout sauf le nom est optionnel — même une simple description génère un Skill utile.

Une fois créé, invoquez le collègue avec `/{slug}`.

### Commandes

| Commande | Description |
|----------|-------------|
| `/create-teammate` | Créer un nouveau Skill de collègue |
| `/list-teammates` | Lister tous les Skills de collègues |
| `/{slug}` | Invoquer le Skill complet (Persona + Travail) |
| `/{slug}-work` | Capacités de travail uniquement |
| `/{slug}-persona` | Persona uniquement |
| `/compare {a} vs {b}` | Comparaison côte à côte avec simulation de scénarios |
| `/export-teammate {slug}` | Exporter un package portable `.tar.gz` pour le partage |
| `/update-teammate {slug}` | Ajouter de nouveaux matériaux à un collègue existant |
| `/teammate-rollback {slug} {version}` | Revenir à une version précédente |
| `/delete-teammate {slug}` | Supprimer un Skill de collègue |

---

## Démo

> Entrée : `Stripe L3 backend engineer, INTJ, perfectionist, Stripe-style, brutal code reviewer`

**Scénario 1 : Revue de code**

```
User              ❯ Can you review this API endpoint?

teammate.skill    ❯ What problem does this actually solve? The PR description
                    doesn't say. Adding that first.
                    
                    Looking at the code: you're using float for the amount
                    field. That's a blocking issue — use Decimal for financial
                    values. Also, this endpoint isn't idempotent. What happens
                    on retry?
```

**Scénario 2 : Discussion de conception**

```
User              ❯ Should we use MongoDB for this new feature?

teammate.skill    ❯ Strong disagree. We need ACID transactions for payment
                    flows. Mongo doesn't give us that. Let's stick with
                    Postgres. If the concern is schema flexibility, we can
                    use JSONB columns.
```

**Scénario 3 : Refus de compromis**

```
User              ❯ Can we skip tests and ship this by Friday?

teammate.skill    ❯ No. We get the tests right or we don't ship. If Friday
                    is a hard deadline, let's cut scope instead of cutting
                    quality. What's the minimum we need for launch?
```

---

## Fonctionnalités

### Structure du Skill généré

Chaque Skill de collègue se compose de deux parties complémentaires :

| Partie | Contenu |
|--------|---------|
| **Part A — Compétences de travail** | Systèmes gérés, standards techniques, workflows, focus CR, expérience |
| **Part B — Persona** | Personnalité à 5 couches : règles strictes → identité → expression → décisions → interpersonnel |

Exécution : `Réception de la tâche → La Persona décide de l'attitude → Les compétences exécutent → Sortie avec leur voix`

### Tags supportés

**Personnalité** : Meticulous · Good-enough · Blame-deflector · Perfectionist · Procrastinator · Ship-fast · Over-engineer · Scope-creeper · Bike-shedder · Micro-manager · Hands-off · Devil's-advocate · Mentor-type · Gatekeeper · Passive-aggressive · Confrontational …

**Culture d'entreprise** : Google-style · Meta-style · Amazon-style · Apple-style · Stripe-style · Netflix-style · Microsoft-style · Startup-mode · Agency-mode · First-principles · Open-source-native

**Niveaux** : Google L3-L11 · Meta E3-E9 · Amazon L4-L10 · Stripe L1-L5 · Microsoft 59-67+ · Apple ICT2-ICT6 · Netflix · Uber · Airbnb · ByteDance · Alibaba · Tencent · Generic (Junior/Senior/Staff/Principal)

### Évolution

- **Ajouter des fichiers** → analyse automatique du delta → fusion dans les sections pertinentes, jamais d'écrasement des conclusions existantes
- **Correction par conversation** → dites « ils ne feraient pas ça, ils feraient plutôt... » → écrit dans la couche de correction, effet immédiat
- **Contrôle de version** → archivage automatique à chaque mise à jour, retour à n'importe quelle version précédente

---

## Assurance qualité

Chaque collègue passe par un **pipeline de qualité à 3 niveaux** avant de vous être livré :

### 1. Porte de qualité (pré-aperçu)
Valide le contenu généré selon 7 règles strictes : concrétude du Layer 0, nombre d'exemples, densité des expressions typiques, ordre des priorités, définition du périmètre, absence de remplissage générique, complétude tag→règle. Les échecs sont auto-corrigés avant que vous ne voyiez l'aperçu.

### 2. Smoke Test (post-création)
Trois prompts de test automatisés sont exécutés contre chaque Skill généré :
- **Question de domaine** — le Skill utilise-t-il de vrais systèmes/outils, et non des conseils génériques ?
- **Scénario de pression** — la persona tient-elle sous la pression, ou s'effondre-t-elle en IA générique ?
- **Question hors périmètre** — le Skill admet-il les limites de ses connaissances dans le personnage ?

```
🧪 Smoke Test: ✅ Domain ✅ Pushback ✅ Out-of-scope — 3/3 passed
```

### 3. Scan de confidentialité (pré-export)
Détection automatique des e-mails, numéros de téléphone, tokens API, numéros de sécurité sociale et autres données personnelles :
```bash
python3 tools/privacy_guard.py --scan teammates/alex-chen/          # détecter
python3 tools/privacy_guard.py --scan teammates/alex-chen/ --redact  # auto-corriger
```

Les fichiers de connaissances brutes (`knowledge/`) sont exclus de git et des exports par défaut.

---

## Comparer des collègues

Comparaison côte à côte avec simulation de scénarios :

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

Supporte également la **simulation de décision** — regardez deux collègues débattre d'une décision technique dans le personnage.

---

## Exporter & Partager

Exportez des collègues en packages portables :

```bash
/export-teammate alex-chen
# → alex-chen.teammate.tar.gz (fichiers de skill uniquement, pas de données brutes)

# Importer sur une autre machine :
tar xzf alex-chen.teammate.tar.gz -C ./teammates/
```

L'export inclut : SKILL.md, work.md, persona.md, meta.json, l'historique des versions et un manifeste.
Les fichiers de connaissances brutes sont exclus par défaut — ajoutez `--include-knowledge` si nécessaire (⚠️ contient des données personnelles).

---

## Structure du projet

Ce projet suit le standard ouvert [AgentSkills](https://agentskills.io) :

```
create-teammate/
├── SKILL.md                  # Point d'entrée du Skill
├── prompts/                  # Modèles de prompts
│   ├── intake.md             #   Collecte d'informations (3 questions)
│   ├── work_analyzer.md      #   Extraction des compétences de travail
│   ├── persona_analyzer.md   #   Extraction de personnalité + traduction des tags
│   ├── work_builder.md       #   Modèle de génération work.md
│   ├── persona_builder.md    #   Structure à 5 couches persona.md
│   ├── merger.md             #   Logique de fusion incrémentale
│   ├── correction_handler.md #   Gestionnaire de corrections par conversation
│   ├── compare.md            #   Comparaison côte à côte de collègues
│   └── smoke_test.md         #   Validation qualité post-création
├── tools/                    # Collecte de données & gestion
│   ├── slack_collector.py    #   Collecteur automatique Slack (Bot Token)
│   ├── slack_parser.py       #   Parseur d'export JSON Slack
│   ├── github_collector.py   #   Collecteur GitHub PR/review
│   ├── teams_parser.py       #   Parseur Teams/Outlook
│   ├── email_parser.py       #   Parseur Gmail .mbox/.eml
│   ├── notion_parser.py      #   Parseur d'export Notion
│   ├── confluence_parser.py  #   Parseur d'export Confluence
│   ├── project_tracker_parser.py # Parseur JIRA/Linear
│   ├── skill_writer.py       #   Gestion des fichiers Skill
│   ├── version_manager.py    #   Archivage de versions & rollback
│   ├── privacy_guard.py      #   Scanner PII & auto-masquage
│   └── export.py             #   Export/import de packages portables
├── teammates/                # Skills de collègues générés
│   └── example_alex/         #   Exemple : Stripe L3 backend engineer
├── docs/
├── requirements.txt
├── INSTALL.md
└── LICENSE
```

---

## Bonnes pratiques

- **Qualité des matériaux source = Qualité du Skill** : vrais logs de conversation + docs de conception > description manuelle seule
- Priorisez la collecte de : **docs de conception qu'ils ont rédigés** > **commentaires de revue de code** > **discussions de décision** > chat informel
- Les PRs et reviews GitHub sont une mine d'or pour les compétences de travail — ils révèlent les standards de code et les priorités de revue réels
- Les fils Slack sont une mine d'or pour la Persona — ils révèlent le style de communication sous différentes pressions
- Commencez par une description manuelle, puis ajoutez progressivement des données réelles au fur et à mesure

---

## Licence

MIT License — voir [LICENSE](LICENSE) pour les détails.

---

<div align="center">

**teammate.skill** — parce que le meilleur transfert de connaissances n'est pas un document, c'est un modèle opérationnel.

</div>
