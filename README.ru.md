[English](README.md) | [简体中文](README.zh-CN.md) | [Français](README.fr.md) | [Deutsch](README.de.md) | [Русский](README.ru.md) | [日本語](README.ja.md) | [Italiano](README.it.md) | [Español](README.es.md)

<div align="center">

<h1><img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=50&duration=3000&pause=1000&color=6C63FF&center=true&vCenter=true&width=600&height=80&lines=teammate.skill" alt="teammate.skill" /></h1>

> *Ваш коллега ушёл. Его контекст мог бы остаться.*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://python.org)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet)](https://claude.ai/code)
[![OpenClaw](https://img.shields.io/badge/OpenClaw-Skill-orange)](https://openclaw.ai)
[![AgentSkills](https://img.shields.io/badge/AgentSkills-Standard-green)](https://agentskills.io)

<br>

Ваш коллега уволился, оставив гору неподдерживаемой документации?<br>
Ваш ведущий инженер ушёл, забрав с собой все «племенные знания»?<br>
Ваш наставник перешёл в другую компанию, и три года контекста испарились за ночь?<br>
Ваш сооснователь сменил роль, а документ передачи дел — две страницы?<br>

**Превращайте уходы в устойчивые Skills. Добро пожаловать в эпоху бессмертия знаний.**

<br>

Предоставьте исходные материалы (сообщения из Slack, PR на GitHub, письма, документы Notion, заметки с совещаний)<br>
плюс ваше описание того, кем они были<br>
и получите **ИИ-Skill, который действительно работает как они**<br>
— пишет код в их стиле, ревьюит PR по их стандартам, отвечает на вопросы их голосом

[Поддерживаемые источники](#поддерживаемые-источники-данных) · [Установка](#установка) · [Использование](#использование) · [Демо](#демо) · [Подробная установка](INSTALL.md)

</div>

---

## Поддерживаемые источники данных

> Beta — скоро появятся новые интеграции!

| Источник | Сообщения | Документы / Wiki | Код & PR | Примечания |
|----------|:---------:|:----------------:|:--------:|------------|
| Slack (автосбор) | ✅ API | — | — | Введите имя пользователя, полностью автоматически |
| GitHub (автосбор) | — | — | ✅ API | PR, ревью, комментарии к issues |
| Slack-экспорт JSON | ✅ | — | — | Ручная загрузка |
| Gmail `.mbox` / `.eml` | ✅ | — | — | Ручная загрузка |
| Teams / Outlook-экспорт | ✅ | — | — | Ручная загрузка |
| Notion-экспорт | — | ✅ | — | HTML- или Markdown-экспорт |
| Confluence-экспорт | — | ✅ | — | HTML-экспорт или zip |
| JIRA CSV / Linear JSON | — | — | ✅ | Экспорт из трекеров задач |
| PDF | — | ✅ | — | Ручная загрузка |
| Изображения / Скриншоты | ✅ | — | — | Ручная загрузка |
| Markdown / Text | ✅ | ✅ | — | Ручная загрузка |
| Вставка текста напрямую | ✅ | — | — | Скопируйте и вставьте что угодно |

---

## Платформы

### [Claude Code](https://claude.ai/code)
Официальный CLI от Anthropic для Claude. Установите этот Skill в `.claude/skills/` и вызывайте командой `/create-teammate`.

### [OpenClaw](https://openclaw.ai) 🦞
Open-source персональный ИИ-ассистент от [@steipete](https://github.com/steipete). Работает на ваших собственных устройствах, отвечает через 25+ каналов (WhatsApp, Telegram, Slack, Discord, Teams, Signal, iMessage и другие). Local-first шлюз, постоянная память, голос, canvas, cron-задачи и растущая экосистема Skills. [GitHub](https://github.com/openclaw/openclaw)

### 🏆 [MyClaw.ai](https://myclaw.ai)
Управляемый хостинг для OpenClaw — забудьте о Docker, серверах и конфигурациях. Развёртывание в один клик, всегда онлайн, автоматические обновления, ежедневные бэкапы. Ваш экземпляр OpenClaw запущен за минуты. Идеально, если вы хотите, чтобы teammate.skill работал 24/7 без самостоятельного хостинга.

---

## Установка

Этот Skill следует открытому стандарту [AgentSkills](https://agentskills.io) и работает с любым совместимым агентом.

### Claude Code

```bash
# Для проекта (в корне git-репозитория)
mkdir -p .claude/skills
git clone https://github.com/LeoYeAI/teammate-skill .claude/skills/create-teammate

# Глобально (все проекты)
git clone https://github.com/LeoYeAI/teammate-skill ~/.claude/skills/create-teammate
```

### OpenClaw

```bash
git clone https://github.com/LeoYeAI/teammate-skill ~/.openclaw/workspace/skills/create-teammate
```

### Другие AgentSkills-совместимые агенты

Клонируйте в директорию Skills вашего агента. Точка входа — `SKILL.md` со стандартным frontmatter — любой агент, поддерживающий формат AgentSkills, подхватит его автоматически.

### Зависимости (опционально)

```bash
pip3 install -r requirements.txt
```

> Автоматический сбор из Slack требует Bot Token. Сбор из GitHub использует `GITHUB_TOKEN`. См. [INSTALL.md](INSTALL.md).

---

## Использование

В вашем агенте (Claude Code, OpenClaw или любом AgentSkills-совместимом агенте) введите:

```
/create-teammate
```

Следуйте подсказкам: введите имя, информацию о роли (например, `Google L5 backend engineer`), теги личности, затем выберите источники данных. Всё, кроме имени, можно пропустить — даже одно описание генерирует полезный Skill.

После создания вызывайте тиммейта командой `/{slug}`.

### Команды

| Команда | Описание |
|---------|----------|
| `/create-teammate` | Создать новый Skill тиммейта |
| `/list-teammates` | Показать список всех Skills тиммейтов |
| `/{slug}` | Вызвать полный Skill (Персона + Работа) |
| `/{slug}-work` | Только рабочие способности |
| `/{slug}-persona` | Только персона |
| `/compare {a} vs {b}` | Сравнение бок о бок с моделированием сценариев |
| `/export-teammate {slug}` | Экспорт портативного пакета `.tar.gz` для обмена |
| `/update-teammate {slug}` | Добавить новые материалы к существующему тиммейту |
| `/teammate-rollback {slug} {version}` | Откатиться к предыдущей версии |
| `/delete-teammate {slug}` | Удалить Skill тиммейта |

---

## Демо

> Ввод: `Stripe L3 backend engineer, INTJ, perfectionist, Stripe-style, brutal code reviewer`

**Сценарий 1: Код-ревью**

```
User              ❯ Can you review this API endpoint?

teammate.skill    ❯ What problem does this actually solve? The PR description
                    doesn't say. Adding that first.
                    
                    Looking at the code: you're using float for the amount
                    field. That's a blocking issue — use Decimal for financial
                    values. Also, this endpoint isn't idempotent. What happens
                    on retry?
```

**Сценарий 2: Обсуждение архитектуры**

```
User              ❯ Should we use MongoDB for this new feature?

teammate.skill    ❯ Strong disagree. We need ACID transactions for payment
                    flows. Mongo doesn't give us that. Let's stick with
                    Postgres. If the concern is schema flexibility, we can
                    use JSONB columns.
```

**Сценарий 3: Отказ от компромисса**

```
User              ❯ Can we skip tests and ship this by Friday?

teammate.skill    ❯ No. We get the tests right or we don't ship. If Friday
                    is a hard deadline, let's cut scope instead of cutting
                    quality. What's the minimum we need for launch?
```

---

## Возможности

### Структура сгенерированного Skill

Каждый Skill тиммейта состоит из двух взаимодополняющих частей:

| Часть | Содержание |
|-------|-----------|
| **Part A — Рабочие навыки** | Системы, технические стандарты, рабочие процессы, фокус CR, опыт |
| **Part B — Персона** | 5-уровневая личность: жёсткие правила → идентичность → выражение → принятие решений → межличностное общение |

Выполнение: `Получить задачу → Персона определяет отношение → Рабочие навыки выполняют → Вывод их голосом`

### Поддерживаемые теги

**Личность**: Meticulous · Good-enough · Blame-deflector · Perfectionist · Procrastinator · Ship-fast · Over-engineer · Scope-creeper · Bike-shedder · Micro-manager · Hands-off · Devil's-advocate · Mentor-type · Gatekeeper · Passive-aggressive · Confrontational …

**Корпоративная культура**: Google-style · Meta-style · Amazon-style · Apple-style · Stripe-style · Netflix-style · Microsoft-style · Startup-mode · Agency-mode · First-principles · Open-source-native

**Уровни**: Google L3-L11 · Meta E3-E9 · Amazon L4-L10 · Stripe L1-L5 · Microsoft 59-67+ · Apple ICT2-ICT6 · Netflix · Uber · Airbnb · ByteDance · Alibaba · Tencent · Generic (Junior/Senior/Staff/Principal)

### Эволюция

- **Добавление файлов** → автоматический анализ дельты → слияние в соответствующие разделы, существующие выводы никогда не перезаписываются
- **Коррекция через диалог** → скажите «они бы так не делали, они бы...» → записывается в слой коррекции, вступает в силу немедленно
- **Контроль версий** → автоматическое архивирование при каждом обновлении, откат на любую предыдущую версию

---

## Контроль качества

Каждый тиммейт проходит **3-уровневый конвейер качества** перед тем, как вы его получите:

### 1. Проверка качества (до предпросмотра)
Валидация сгенерированного контента по 7 жёстким правилам: конкретность Layer 0, количество примеров, плотность характерных выражений, порядок приоритетов, определение области, отсутствие шаблонного заполнителя, полнота тег→правило. Ошибки автоматически исправляются до того, как вы увидите предпросмотр.

### 2. Smoke Test (после создания)
Три автоматических тестовых промпта запускаются против каждого сгенерированного Skill:
- **Вопрос по домену** — использует ли Skill реальные системы/инструменты, а не общие советы?
- **Сценарий давления** — держится ли персона под давлением или скатывается в обобщённый ИИ?
- **Вопрос за пределами области** — признаёт ли Skill границы знаний в характере персонажа?

```
🧪 Smoke Test: ✅ Domain ✅ Pushback ✅ Out-of-scope — 3/3 passed
```

### 3. Сканирование приватности (до экспорта)
Автоматическое обнаружение email-адресов, номеров телефонов, API-токенов, SSN и других персональных данных:
```bash
python3 tools/privacy_guard.py --scan teammates/alex-chen/          # обнаружить
python3 tools/privacy_guard.py --scan teammates/alex-chen/ --redact  # авто-исправить
```

Сырые файлы знаний (`knowledge/`) по умолчанию исключены из git и экспортов.

---

## Сравнение тиммейтов

Сравнение бок о бок с моделированием сценариев:

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

Также поддерживает **симуляцию принятия решений** — наблюдайте, как два тиммейта спорят о техническом решении в характере.

---

## Экспорт и обмен

Экспортируйте тиммейтов как портативные пакеты:

```bash
/export-teammate alex-chen
# → alex-chen.teammate.tar.gz (только файлы Skill, без сырых данных)

# Импорт на другой машине:
tar xzf alex-chen.teammate.tar.gz -C ./teammates/
```

Экспорт включает: SKILL.md, work.md, persona.md, meta.json, историю версий и манифест.
Сырые файлы знаний по умолчанию исключены — добавьте `--include-knowledge` при необходимости (⚠️ содержит персональные данные).

---

## Структура проекта

Проект следует открытому стандарту [AgentSkills](https://agentskills.io):

```
create-teammate/
├── SKILL.md                  # Точка входа Skill
├── prompts/                  # Шаблоны промптов
│   ├── intake.md             #   Сбор информации (3 вопроса)
│   ├── work_analyzer.md      #   Извлечение рабочих навыков
│   ├── persona_analyzer.md   #   Извлечение личности + перевод тегов
│   ├── work_builder.md       #   Шаблон генерации work.md
│   ├── persona_builder.md    #   5-уровневая структура persona.md
│   ├── merger.md             #   Логика инкрементального слияния
│   ├── correction_handler.md #   Обработчик коррекции через диалог
│   ├── compare.md            #   Сравнение тиммейтов бок о бок
│   └── smoke_test.md         #   Валидация качества после создания
├── tools/                    # Сбор данных & управление
│   ├── slack_collector.py    #   Автосборщик Slack (Bot Token)
│   ├── slack_parser.py       #   Парсер JSON-экспорта Slack
│   ├── github_collector.py   #   Сборщик GitHub PR/review
│   ├── teams_parser.py       #   Парсер Teams/Outlook
│   ├── email_parser.py       #   Парсер Gmail .mbox/.eml
│   ├── notion_parser.py      #   Парсер экспорта Notion
│   ├── confluence_parser.py  #   Парсер экспорта Confluence
│   ├── project_tracker_parser.py # Парсер JIRA/Linear
│   ├── skill_writer.py       #   Управление файлами Skill
│   ├── version_manager.py    #   Архивация версий & откат
│   ├── privacy_guard.py      #   Сканер PII & авто-маскирование
│   └── export.py             #   Экспорт/импорт портативных пакетов
├── teammates/                # Сгенерированные Skills тиммейтов
│   └── example_alex/         #   Пример: Stripe L3 бэкенд-инженер
├── docs/
├── requirements.txt
├── INSTALL.md
└── LICENSE
```

---

## Лучшие практики

- **Качество исходных материалов = Качество Skill**: реальные логи чатов + проектные документы > только ручное описание
- Приоритет сбора: **проектные документы, которые они написали** > **комментарии к код-ревью** > **обсуждения решений** > обычный чат
- PR и ревью на GitHub — золотая жила для рабочих навыков: они раскрывают реальные стандарты кодирования и приоритеты ревью
- Треды в Slack — золотая жила для персоны: они показывают стиль общения под разным давлением
- Начните с ручного описания, затем постепенно добавляйте реальные данные по мере их обнаружения

---

## Лицензия

MIT License — подробности в [LICENSE](LICENSE).

---

<div align="center">

**teammate.skill** — потому что лучший способ передачи знаний — это не документ, а рабочая модель.

</div>
