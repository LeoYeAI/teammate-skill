[English](README.md) | [简体中文](README.zh-CN.md) | [Français](README.fr.md) | [Deutsch](README.de.md) | [Русский](README.ru.md) | [日本語](README.ja.md) | [Italiano](README.it.md) | [Español](README.es.md)

<div align="center">

<h1><img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=50&duration=3000&pause=1000&color=6C63FF&center=true&vCenter=true&width=600&height=80&lines=teammate.skill" alt="teammate.skill" /></h1>

> *Il tuo collega se n'è andato. Il suo contesto non doveva fare la stessa fine.*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://python.org)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet)](https://claude.ai/code)
[![OpenClaw](https://img.shields.io/badge/OpenClaw-Skill-orange)](https://openclaw.ai)
[![AgentSkills](https://img.shields.io/badge/AgentSkills-Standard-green)](https://agentskills.io)

<br>

Il tuo collega si è licenziato, lasciandosi dietro una montagna di documentazione non mantenuta?<br>
Il tuo ingegnere senior se n'è andato, portandosi via tutta la conoscenza tribale?<br>
Il tuo mentore è passato oltre, e tre anni di contesto sono svaniti da un giorno all'altro?<br>
Il tuo co-fondatore ha cambiato ruolo, e il documento di passaggio di consegne è di due pagine?<br>

**Trasforma le partenze in Skill durevoli. Benvenuto nell'immortalità della conoscenza.**

<br>

Fornisci i materiali sorgente (messaggi Slack, PR GitHub, email, documenti Notion, appunti delle riunioni)<br>
più la tua descrizione di chi è quella persona<br>
e ottieni una **Skill IA che funziona davvero come loro**<br>
— scrive codice nel loro stile, revisiona PR con i loro standard, risponde alle domande con la loro voce

[Fonti supportate](#fonti-dati-supportate) · [Installazione](#installazione) · [Utilizzo](#utilizzo) · [Demo](#demo) · [Installazione dettagliata](INSTALL.md)

</div>

---

## Fonti dati supportate

> Beta — nuove integrazioni in arrivo!

| Fonte | Messaggi | Documenti / Wiki | Codice e PR | Note |
|-------|:--------:|:-----------------:|:-----------:|------|
| Slack (raccolta automatica) | ✅ API | — | — | Inserisci il nome utente, completamente automatico |
| GitHub (raccolta automatica) | — | — | ✅ API | PR, review, commenti sulle issue |
| Slack export JSON | ✅ | — | — | Caricamento manuale |
| Gmail `.mbox` / `.eml` | ✅ | — | — | Caricamento manuale |
| Teams / Outlook export | ✅ | — | — | Caricamento manuale |
| Notion export | — | ✅ | — | Export HTML o Markdown |
| Confluence export | — | ✅ | — | Export HTML o zip |
| JIRA CSV / Linear JSON | — | — | ✅ | Export di issue tracker |
| PDF | — | ✅ | — | Caricamento manuale |
| Immagini / Screenshot | ✅ | — | — | Caricamento manuale |
| Markdown / Text | ✅ | ✅ | — | Caricamento manuale |
| Incolla testo direttamente | ✅ | — | — | Copia-incolla qualsiasi cosa |

---

## Piattaforme

### [Claude Code](https://claude.ai/code)
La CLI ufficiale di Anthropic per Claude. Installa questa skill in `.claude/skills/` e invocala con `/create-teammate`.

### 🦞 [OpenClaw](https://openclaw.ai)
Assistente IA personale open-source di [@steipete](https://github.com/steipete). Gira sui tuoi dispositivi, risponde su oltre 25 canali (WhatsApp, Telegram, Slack, Discord, Teams, Signal, iMessage e altri). Gateway locale, memoria persistente, voce, canvas, cron job e un ecosistema di skill in crescita. [GitHub](https://github.com/openclaw/openclaw)

### 🏆 [MyClaw.ai](https://myclaw.ai)
Hosting gestito per OpenClaw — niente Docker, server o configurazioni. Deploy con un click, sempre attivo, aggiornamenti automatici, backup giornalieri. La tua istanza OpenClaw online in pochi minuti. Perfetto se vuoi teammate.skill attivo 24/7 senza self-hosting.

---

## Installazione

Questa skill segue lo standard aperto [AgentSkills](https://agentskills.io) e funziona con qualsiasi agente compatibile.

### Claude Code

```bash
# Per progetto (nella root del repository git)
mkdir -p .claude/skills
git clone https://github.com/LeoYeAI/teammate-skill .claude/skills/create-teammate

# Globale (tutti i progetti)
git clone https://github.com/LeoYeAI/teammate-skill ~/.claude/skills/create-teammate
```

### OpenClaw

```bash
git clone https://github.com/LeoYeAI/teammate-skill ~/.openclaw/workspace/skills/create-teammate
```

### Altri agenti compatibili con AgentSkills

Clona nella directory delle skill del tuo agente. Il punto di ingresso è `SKILL.md` con frontmatter standard — qualsiasi agente che legge il formato AgentSkills lo rileverà automaticamente.

### Dipendenze (opzionali)

```bash
pip3 install -r requirements.txt
```

> La raccolta automatica da Slack richiede un Bot Token. La raccolta da GitHub usa `GITHUB_TOKEN`. Vedi [INSTALL.md](INSTALL.md).

---

## Utilizzo

Nel tuo agente (Claude Code, OpenClaw o qualsiasi agente compatibile con AgentSkills), digita:

```
/create-teammate
```

Segui le istruzioni: inserisci un nome, informazioni sul ruolo (es. `Google L5 backend engineer`), tag di personalità, poi scegli le fonti dati. Tutto tranne il nome è facoltativo — anche solo una descrizione genera una Skill utile.

Una volta creata, invoca il teammate con `/{slug}`.

### Comandi

| Comando | Descrizione |
|---------|-------------|
| `/create-teammate` | Crea una nuova Skill teammate |
| `/list-teammates` | Elenca tutte le Skill teammate |
| `/{slug}` | Invoca la Skill completa (Persona + Lavoro) |
| `/{slug}-work` | Solo capacità lavorative |
| `/{slug}-persona` | Solo persona |
| `/compare {a} vs {b}` | Confronto affiancato con simulazione di scenari |
| `/export-teammate {slug}` | Esporta pacchetto portabile `.tar.gz` per la condivisione |
| `/update-teammate {slug}` | Aggiungi nuovi materiali a un teammate esistente |
| `/teammate-rollback {slug} {version}` | Ripristina una versione precedente |
| `/delete-teammate {slug}` | Elimina una Skill teammate |

---

## Demo

> Input: `Stripe L3 backend engineer, INTJ, perfezionista, stile Stripe, revisore di codice spietato`

**Scenario 1: Code Review**

```
Utente              ❯ Puoi revisionare questo endpoint API?

teammate.skill      ❯ Che problema risolve esattamente? La descrizione della PR
                      non lo dice. Prima aggiungiamo quello.
                      
                      Guardando il codice: stai usando float per il campo
                      amount. Questo è un problema bloccante — usa Decimal per
                      i valori finanziari. Inoltre, questo endpoint non è
                      idempotente. Cosa succede in caso di retry?
```

**Scenario 2: Discussione di design**

```
Utente              ❯ Dovremmo usare MongoDB per questa nuova feature?

teammate.skill      ❯ Fortemente contrario. Ci servono transazioni ACID per i
                      flussi di pagamento. Mongo non ce le offre. Restiamo con
                      Postgres. Se la preoccupazione è la flessibilità dello
                      schema, possiamo usare colonne JSONB.
```

**Scenario 3: Opposizione**

```
Utente              ❯ Possiamo saltare i test e rilasciare entro venerdì?

teammate.skill      ❯ No. O facciamo i test come si deve o non rilasciamo. Se
                      venerdì è una scadenza tassativa, riduciamo lo scope
                      invece di ridurre la qualità. Qual è il minimo
                      indispensabile per il lancio?
```

---

## Funzionalità

### Struttura della Skill generata

Ogni Skill teammate è composta da due parti che lavorano insieme:

| Parte | Contenuto |
|-------|-----------|
| **Parte A — Work Skill** | Sistemi gestiti, standard tecnici, workflow, focus nella CR, esperienza |
| **Parte B — Persona** | Personalità a 5 livelli: regole rigide → identità → espressione → decisioni → relazioni interpersonali |

Esecuzione: `Ricevi task → La Persona decide l'atteggiamento → La Work Skill esegue → Output con la loro voce`

### Tag supportati

**Personalità**: Meticulous · Good-enough · Blame-deflector · Perfectionist · Procrastinator · Ship-fast · Over-engineer · Scope-creeper · Bike-shedder · Micro-manager · Hands-off · Devil's-advocate · Mentor-type · Gatekeeper · Passive-aggressive · Confrontational …

**Cultura aziendale**: Google-style · Meta-style · Amazon-style · Apple-style · Stripe-style · Netflix-style · Microsoft-style · Startup-mode · Agency-mode · First-principles · Open-source-native

**Livelli**: Google L3-L11 · Meta E3-E9 · Amazon L4-L10 · Stripe L1-L5 · Microsoft 59-67+ · Apple ICT2-ICT6 · Netflix · Uber · Airbnb · ByteDance · Alibaba · Tencent · Generic (Junior/Senior/Staff/Principal)

### Evoluzione

- **Aggiungi file** → analisi automatica del delta → merge nelle sezioni pertinenti, senza mai sovrascrivere le conclusioni esistenti
- **Correzione conversazionale** → dì "loro non farebbero così, farebbero..." → scrive nel livello di Correzione, con effetto immediato
- **Controllo versioni** → archiviazione automatica ad ogni aggiornamento, rollback a qualsiasi versione precedente

---

## Garanzia di Qualità

Ogni teammate passa attraverso una **pipeline di qualità a 3 livelli** prima della consegna:

### 1. Quality Gate (pre-anteprima)
Valida il contenuto generato su 7 regole: concretezza Layer 0, conteggio esempi, densità catchphrase, ordinamento priorità, definizione scope, nessun testo generico, completezza traduzione tag→regola. I problemi vengono corretti automaticamente prima dell'anteprima.

### 2. Smoke Test (post-creazione)
Tre prompt di test automatici eseguiti su ogni skill generata:
- **Domanda di dominio** — la skill usa sistemi/strumenti reali, non consigli generici?
- **Scenario di opposizione** — la persona regge sotto pressione, o crolla in AI generico?
- **Domanda fuori ambito** — la skill ammette i limiti di conoscenza restando nel personaggio?

```
🧪 Smoke Test: ✅ Dominio ✅ Opposizione ✅ Fuori ambito — 3/3 superati
```

### 3. Scansione Privacy (pre-esportazione)
Rilevamento automatico di email, numeri di telefono, token API, codici fiscali e altri dati sensibili:
```bash
python3 tools/privacy_guard.py --scan teammates/alex-chen/          # rileva
python3 tools/privacy_guard.py --scan teammates/alex-chen/ --redact  # correggi
```

I file di conoscenza grezzi (`knowledge/`) sono esclusi da git e dalle esportazioni per impostazione predefinita.

---

## Confronta Teammate

Confronto affiancato con simulazione di scenari:

```
Tu     ❯  /compare alex-chen vs bob-smith

Agent  ❯  ━━━ alex-chen vs bob-smith ━━━
                         alex-chen              bob-smith
          Priorità:      Correttezza > Velocità Ship fast > Perfetto
          Stile CR:      Bloccante sui nomi      Solo suggerimenti
          Sotto pressione: Diventa più silenzioso Diventa più rumoroso

Tu     ❯  Chi dovrebbe revisionare il redesign dell'API pagamenti?

Agent  ❯  alex-chen: "Mandami il design doc. Voglio controllare
             idempotenza e contratti di errore."
          bob-smith: "Facciamo una call e lo vediamo insieme."

          Raccomandazione: alex-chen per il rigore sulla correttezza.
```

Supporta anche **simulazione di decisioni** — guarda due teammate discutere una decisione tecnica restando nel personaggio.

---

## Esporta e Condividi

Esporta teammate come pacchetti portabili:

```bash
/export-teammate alex-chen
# → alex-chen.teammate.tar.gz (solo file skill, nessun dato grezzo)

# Importa su un'altra macchina:
tar xzf alex-chen.teammate.tar.gz -C ./teammates/
```

L'esportazione include: SKILL.md, work.md, persona.md, meta.json, cronologia versioni e un manifesto.
I file di conoscenza grezzi sono esclusi per impostazione predefinita — aggiungi `--include-knowledge` se necessario (⚠️ contiene dati personali).

---

## Struttura del progetto

Questo progetto segue lo standard aperto [AgentSkills](https://agentskills.io):

```
create-teammate/
├── SKILL.md                      # Punto di ingresso della Skill
├── prompts/                      # Template dei prompt
│   ├── intake.md                 #   Raccolta informazioni (3 domande)
│   ├── work_analyzer.md          #   Estrazione capacità lavorative
│   ├── persona_analyzer.md       #   Estrazione personalità + traduzione tag
│   ├── work_builder.md           #   Template di generazione work.md
│   ├── persona_builder.md        #   Struttura a 5 livelli di persona.md
│   ├── merger.md                 #   Logica di merge incrementale
│   ├── correction_handler.md     #   Gestore correzioni conversazionali
│   ├── compare.md                #   Confronto affiancato teammate
│   └── smoke_test.md             #   Validazione qualità post-creazione
├── tools/                        # Raccolta dati e gestione
│   ├── slack_collector.py        #   Raccoglitore automatico Slack (Bot Token)
│   ├── slack_parser.py           #   Parser per export JSON di Slack
│   ├── github_collector.py       #   Raccoglitore PR/review GitHub
│   ├── teams_parser.py           #   Parser Teams/Outlook
│   ├── email_parser.py           #   Parser Gmail .mbox/.eml
│   ├── notion_parser.py          #   Parser export Notion
│   ├── confluence_parser.py      #   Parser export Confluence
│   ├── project_tracker_parser.py #   Parser JIRA/Linear
│   ├── skill_writer.py           #   Gestione file della Skill
│   ├── version_manager.py        #   Archiviazione versioni e rollback
│   ├── privacy_guard.py          #   Scanner PII e auto-redazione
│   └── export.py                 #   Esportazione/importazione pacchetti
├── teammates/                    # Skill teammate generate
│   └── example_alex/             #   Esempio: Stripe L3 backend engineer
├── requirements.txt
├── INSTALL.md
└── LICENSE
```

---

## Buone pratiche

- **Qualità del materiale sorgente = qualità della Skill**: log di chat reali + documenti di design > solo descrizione manuale
- Dai priorità alla raccolta di: **documenti di design da loro scritti** > **commenti di code review** > **discussioni sulle decisioni** > chat informali
- Le PR e le review su GitHub sono una miniera d'oro per la Work Skill — rivelano gli standard di codice effettivi e le priorità nelle revisioni
- I thread Slack sono una miniera d'oro per la Persona — rivelano lo stile comunicativo sotto diverse pressioni
- Inizia con una descrizione manuale, poi aggiungi dati reali incrementalmente man mano che li trovi

---

## Licenza

Licenza MIT — vedi [LICENSE](LICENSE) per i dettagli.

---

<div align="center">

**teammate.skill** — perché il miglior trasferimento di conoscenza non è un documento, è un modello funzionante.

</div>
