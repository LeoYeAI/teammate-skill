[English](README.md) | [简体中文](README.zh-CN.md) | [Français](README.fr.md) | [Deutsch](README.de.md) | [Русский](README.ru.md) | [日本語](README.ja.md) | [Italiano](README.it.md) | [Español](README.es.md)

<div align="center">

<h1><img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=50&duration=3000&pause=1000&color=6C63FF&center=true&vCenter=true&width=600&height=80&lines=teammate.skill" alt="teammate.skill" /></h1>

> *Tu compañero se fue. Su contexto no tenía por qué irse también.*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://python.org)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet)](https://claude.ai/code)
[![OpenClaw](https://img.shields.io/badge/OpenClaw-Skill-orange)](https://openclaw.ai)
[![AgentSkills](https://img.shields.io/badge/AgentSkills-Standard-green)](https://agentskills.io)

<br>

¿Tu compañero renunció y dejó una montaña de documentación sin mantener?<br>
¿Tu ingeniero senior se fue y se llevó todo el conocimiento tribal con él?<br>
¿Tu mentor pasó a otra cosa y tres años de contexto desaparecieron de la noche a la mañana?<br>
¿Tu cofundador cambió de rol y el documento de traspaso tiene solo dos páginas?<br>

**Convierte las salidas en Skills duraderos. Bienvenido a la inmortalidad del conocimiento.**

<br>

Proporciona materiales fuente (mensajes de Slack, PRs de GitHub, correos electrónicos, documentos de Notion, notas de reuniones)<br>
más tu descripción de quién es esa persona<br>
y obtén un **Skill de IA que realmente funciona como ellos**<br>
— escribe código con su estilo, revisa PRs con sus estándares, responde preguntas con su voz

[Fuentes compatibles](#fuentes-de-datos-compatibles) · [Instalación](#instalación) · [Uso](#uso) · [Demo](#demo) · [Instalación detallada](INSTALL.md)

</div>

---

## Fuentes de datos compatibles

> Beta — ¡más integraciones próximamente!

| Fuente | Mensajes | Docs / Wiki | Código y PRs | Notas |
|--------|:--------:|:-----------:|:------------:|-------|
| Slack (recolección automática) | ✅ API | — | — | Ingresa el nombre de usuario, totalmente automático |
| GitHub (recolección automática) | — | — | ✅ API | PRs, revisiones, comentarios en issues |
| Slack export JSON | ✅ | — | — | Carga manual |
| Gmail `.mbox` / `.eml` | ✅ | — | — | Carga manual |
| Teams / Outlook export | ✅ | — | — | Carga manual |
| Notion export | — | ✅ | — | Exportación en HTML o Markdown |
| Confluence export | — | ✅ | — | Exportación en HTML o zip |
| JIRA CSV / Linear JSON | — | — | ✅ | Exportaciones de seguimiento de issues |
| PDF | — | ✅ | — | Carga manual |
| Imágenes / Capturas de pantalla | ✅ | — | — | Carga manual |
| Markdown / Text | ✅ | ✅ | — | Carga manual |
| Pegar texto directamente | ✅ | — | — | Copia y pega lo que sea |

---

## Plataformas

### [Claude Code](https://claude.ai/code)
El CLI oficial de Anthropic para Claude. Instala este skill en `.claude/skills/` e invócalo con `/create-teammate`.

### 🦞 [OpenClaw](https://openclaw.ai)
Asistente personal de IA de código abierto creado por [@steipete](https://github.com/steipete). Se ejecuta en tus propios dispositivos, responde en más de 25 canales (WhatsApp, Telegram, Slack, Discord, Teams, Signal, iMessage y más). Gateway local, memoria persistente, voz, canvas, tareas programadas y un ecosistema de skills en crecimiento. [GitHub](https://github.com/openclaw/openclaw)

### 🏆 [MyClaw.ai](https://myclaw.ai)
Hosting gestionado para OpenClaw — olvídate de Docker, servidores y configuraciones. Despliegue con un clic, siempre activo, actualizaciones automáticas, respaldos diarios. Tu instancia de OpenClaw funcionando en minutos. Perfecto si quieres teammate.skill ejecutándose 24/7 sin autohospedaje.

---

## Instalación

Este skill sigue el estándar abierto [AgentSkills](https://agentskills.io) y funciona con cualquier agente compatible.

### Claude Code

```bash
# Por proyecto (en la raíz del repositorio git)
mkdir -p .claude/skills
git clone https://github.com/LeoYeAI/teammate-skill .claude/skills/create-teammate

# Global (todos los proyectos)
git clone https://github.com/LeoYeAI/teammate-skill ~/.claude/skills/create-teammate
```

### OpenClaw

```bash
git clone https://github.com/LeoYeAI/teammate-skill ~/.openclaw/workspace/skills/create-teammate
```

### Otros agentes compatibles con AgentSkills

Clona en el directorio de skills de tu agente. El punto de entrada es `SKILL.md` con frontmatter estándar — cualquier agente que lea el formato AgentSkills lo detectará automáticamente.

### Dependencias (opcional)

```bash
pip3 install -r requirements.txt
```

> La recolección automática de Slack requiere un Bot Token. La recolección de GitHub usa `GITHUB_TOKEN`. Consulta [INSTALL.md](INSTALL.md).

---

## Uso

En tu agente (Claude Code, OpenClaw o cualquier agente compatible con AgentSkills), escribe:

```
/create-teammate
```

Sigue las indicaciones: ingresa un nombre, información del rol (ej. `Google L5 backend engineer`), etiquetas de personalidad, y luego elige las fuentes de datos. Todo excepto el nombre se puede omitir — incluso solo una descripción genera un Skill útil.

Una vez creado, invoca al compañero con `/{slug}`.

### Comandos

| Comando | Descripción |
|---------|-------------|
| `/create-teammate` | Crear un nuevo Skill de compañero |
| `/list-teammates` | Listar todos los Skills de compañeros |
| `/{slug}` | Invocar Skill completo (Persona + Trabajo) |
| `/{slug}-work` | Solo capacidades de trabajo |
| `/{slug}-persona` | Solo personalidad |
| `/compare {a} vs {b}` | Comparación lado a lado con simulación de escenarios |
| `/export-teammate {slug}` | Exportar paquete portátil `.tar.gz` para compartir |
| `/teammate-rollback {slug} {version}` | Revertir a una versión anterior |
| `/delete-teammate {slug}` | Eliminar un Skill de compañero |

---

## Demo

> Entrada: `Stripe L3 backend engineer, INTJ, perfectionist, Stripe-style, brutal code reviewer`

**Escenario 1: Revisión de código**

```
User              ❯ Can you review this API endpoint?

teammate.skill    ❯ What problem does this actually solve? The PR description
                    doesn't say. Adding that first.
                    
                    Looking at the code: you're using float for the amount
                    field. That's a blocking issue — use Decimal for financial
                    values. Also, this endpoint isn't idempotent. What happens
                    on retry?
```

**Escenario 2: Discusión de diseño**

```
User              ❯ Should we use MongoDB for this new feature?

teammate.skill    ❯ Strong disagree. We need ACID transactions for payment
                    flows. Mongo doesn't give us that. Let's stick with
                    Postgres. If the concern is schema flexibility, we can
                    use JSONB columns.
```

**Escenario 3: Resistencia**

```
User              ❯ Can we skip tests and ship this by Friday?

teammate.skill    ❯ No. We get the tests right or we don't ship. If Friday
                    is a hard deadline, let's cut scope instead of cutting
                    quality. What's the minimum we need for launch?
```

---

## Características

### Estructura del Skill generado

Cada Skill de compañero tiene dos partes que funcionan juntas:

| Parte | Contenido |
|-------|-----------|
| **Parte A — Work Skill** | Sistemas a cargo, estándares técnicos, flujos de trabajo, enfoque de CR, experiencia |
| **Parte B — Persona** | Personalidad en 5 capas: reglas duras → identidad → expresión → decisiones → interpersonal |

Ejecución: `Recibir tarea → Persona decide la actitud → Work Skill ejecuta → Salida con su voz`

### Etiquetas compatibles

**Personalidad**: Meticulous · Good-enough · Blame-deflector · Perfectionist · Procrastinator · Ship-fast · Over-engineer · Scope-creeper · Bike-shedder · Micro-manager · Hands-off · Devil's-advocate · Mentor-type · Gatekeeper · Passive-aggressive · Confrontational …

**Cultura corporativa**: Google-style · Meta-style · Amazon-style · Apple-style · Stripe-style · Netflix-style · Microsoft-style · Startup-mode · Agency-mode · First-principles · Open-source-native

**Niveles**: Google L3-L11 · Meta E3-E9 · Amazon L4-L10 · Stripe L1-L5 · Microsoft 59-67+ · Apple ICT2-ICT6 · Netflix · Uber · Airbnb · ByteDance · Alibaba · Tencent · Genérico (Junior/Senior/Staff/Principal)

### Evolución

- **Agregar archivos** → análisis automático del delta → fusión en las secciones relevantes, nunca sobreescribe conclusiones existentes
- **Corrección en conversación** → di "ellos no harían eso, ellos harían..." → se escribe en la capa de Corrección, toma efecto inmediatamente
- **Control de versiones** → archivo automático en cada actualización, reversión a cualquier versión anterior

---

## Garantía de Calidad

Cada compañero pasa por un **pipeline de calidad de 3 niveles** antes de la entrega:

### 1. Quality Gate (pre-vista previa)
Valida el contenido generado contra 7 reglas: concreción de Layer 0, cantidad de ejemplos, densidad de catchphrases, ordenamiento de prioridades, definición de alcance, sin relleno genérico, completitud de traducción tag→regla. Los fallos se corrigen automáticamente antes de la vista previa.

### 2. Smoke Test (post-creación)
Tres prompts de prueba automatizados ejecutados contra cada skill generada:
- **Pregunta de dominio** — ¿la skill usa sistemas/herramientas reales, no consejos genéricos?
- **Escenario de oposición** — ¿la persona resiste bajo presión, o colapsa en AI genérico?
- **Pregunta fuera de alcance** — ¿la skill admite límites de conocimiento manteniéndose en personaje?

```
🧪 Smoke Test: ✅ Dominio ✅ Oposición ✅ Fuera de alcance — 3/3 superados
```

### 3. Escaneo de Privacidad (pre-exportación)
Detección automática de emails, números de teléfono, tokens de API, y otros datos sensibles:
```bash
python3 tools/privacy_guard.py --scan teammates/alex-chen/          # detectar
python3 tools/privacy_guard.py --scan teammates/alex-chen/ --redact  # corregir
```

Los archivos de conocimiento bruto (`knowledge/`) están excluidos de git y exportaciones por defecto.

---

## Comparar Compañeros

Comparación lado a lado con simulación de escenarios:

```
Tú     ❯  /compare alex-chen vs bob-smith

Agent  ❯  ━━━ alex-chen vs bob-smith ━━━
                         alex-chen              bob-smith
          Prioridad:     Corrección > Velocidad  Ship fast > Perfecto
          Estilo CR:     Bloquea por nombres     Solo sugerencias
          Bajo presión:  Se vuelve más callado   Se vuelve más ruidoso

Tú     ❯  ¿Quién debería revisar el rediseño de la API de pagos?

Agent  ❯  alex-chen: "Mándame el design doc. Quiero revisar
             idempotencia y contratos de error."
          bob-smith: "Hagamos una call y lo vemos juntos."

          Recomendación: alex-chen para rigor en corrección.
```

También soporta **simulación de decisiones** — observa a dos compañeros debatir una decisión técnica en personaje.

---

## Exportar y Compartir

Exporta compañeros como paquetes portátiles:

```bash
/export-teammate alex-chen
# → alex-chen.teammate.tar.gz (solo archivos de skill, sin datos brutos)

# Importar en otra máquina:
tar xzf alex-chen.teammate.tar.gz -C ./teammates/
```

La exportación incluye: SKILL.md, work.md, persona.md, meta.json, historial de versiones y un manifiesto.
Los archivos de conocimiento bruto se excluyen por defecto — añade `--include-knowledge` si es necesario (⚠️ contiene datos personales).

---

## Estructura del proyecto

Este proyecto sigue el estándar abierto [AgentSkills](https://agentskills.io):

```
create-teammate/
├── SKILL.md                      # Punto de entrada del Skill
├── prompts/                      # Plantillas de prompts
│   ├── intake.md                 #   Recolección de información (3 preguntas)
│   ├── work_analyzer.md          #   Extracción de capacidades de trabajo
│   ├── persona_analyzer.md       #   Extracción de personalidad + traducción de etiquetas
│   ├── work_builder.md           #   Plantilla de generación de work.md
│   ├── persona_builder.md        #   Estructura de 5 capas de persona.md
│   ├── merger.md                 #   Lógica de fusión incremental
│   ├── correction_handler.md     #   Manejador de correcciones en conversación
│   ├── compare.md                #   Comparación lado a lado de compañeros
│   └── smoke_test.md             #   Validación de calidad post-creación
├── tools/                        # Recolección de datos y gestión
│   ├── slack_collector.py        #   Recolector automático de Slack (Bot Token)
│   ├── slack_parser.py           #   Parser de exportación JSON de Slack
│   ├── github_collector.py       #   Recolector de PRs/revisiones de GitHub
│   ├── teams_parser.py           #   Parser de Teams/Outlook
│   ├── email_parser.py           #   Parser de Gmail .mbox/.eml
│   ├── notion_parser.py          #   Parser de exportación de Notion
│   ├── confluence_parser.py      #   Parser de exportación de Confluence
│   ├── project_tracker_parser.py #   Parser de JIRA/Linear
│   ├── skill_writer.py           #   Gestión de archivos de Skill
│   ├── version_manager.py        #   Archivo de versiones y reversión
│   ├── privacy_guard.py          #   Escáner PII y auto-redacción
│   └── export.py                 #   Exportación/importación de paquetes
├── teammates/                    # Skills de compañeros generados
│   └── example_alex/             #   Ejemplo: Stripe L3 backend engineer
├── requirements.txt
├── INSTALL.md
└── LICENSE
```

---

## Mejores prácticas

- **Calidad del material fuente = Calidad del Skill**: registros de chat reales + documentos de diseño > solo descripción manual
- Prioriza recolectar: **documentos de diseño que escribieron** > **comentarios de revisión de código** > **discusiones de decisiones** > chat casual
- Los PRs y revisiones de GitHub son minas de oro para el Work Skill — revelan estándares de código reales y prioridades de revisión
- Los hilos de Slack son minas de oro para la Persona — revelan el estilo de comunicación bajo diferentes presiones
- Empieza con una descripción manual, luego agrega datos reales incrementalmente a medida que los encuentres

---

## Licencia

Licencia MIT — consulta [LICENSE](LICENSE) para más detalles.

---

<div align="center">

**teammate.skill** — porque la mejor transferencia de conocimiento no es un documento, es un modelo funcional.

</div>
