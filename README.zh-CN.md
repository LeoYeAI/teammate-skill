[English](README.md) | [简体中文](README.zh-CN.md) | [Français](README.fr.md) | [Deutsch](README.de.md) | [Русский](README.ru.md) | [日本語](README.ja.md) | [Italiano](README.it.md) | [Español](README.es.md)

<div align="center">

<h1><img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=50&duration=3000&pause=1000&color=6C63FF&center=true&vCenter=true&width=600&height=80&lines=teammate.skill" alt="teammate.skill" /></h1>

> *你的队友走了，但他们的经验不必跟着消失。*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://python.org)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet)](https://claude.ai/code)
[![OpenClaw](https://img.shields.io/badge/OpenClaw-Skill-orange)](https://openclaw.ai)
[![AgentSkills](https://img.shields.io/badge/AgentSkills-Standard-green)](https://agentskills.io)

<br>

你的队友离职了，留下一堆无人维护的文档？<br>
你的资深工程师走了，带走了所有只存在于脑子里的知识？<br>
你的导师离开了，三年的经验积累一夜蒸发？<br>
你的联合创始人转岗了，交接文档只有两页？<br>

**把离职变成持久的 Skill。欢迎来到知识永生的时代。**

<br>

提供源材料（Slack 消息、GitHub PR、邮件、Notion 文档、会议记录）<br>
加上你对他们的描述<br>
就能得到一个**真正像他们一样工作的 AI Skill**<br>
——用他们的风格写代码、按他们的标准审 PR、用他们的语气回答问题

[支持的数据源](#支持的数据源) · [安装](#安装) · [使用方法](#使用方法) · [演示](#演示) · [详细安装指南](INSTALL.md)

</div>

---

## 支持的数据源

> Beta — 更多集成即将推出！

| 来源 | 消息 | 文档 / Wiki | 代码 & PR | 备注 |
|------|:----:|:-----------:|:---------:|------|
| Slack（自动采集） | ✅ API | — | — | 输入用户名，全自动采集 |
| GitHub（自动采集） | — | — | ✅ API | PR、Review、Issue 评论 |
| Slack 导出 JSON | ✅ | — | — | 手动上传 |
| Gmail `.mbox` / `.eml` | ✅ | — | — | 手动上传 |
| Teams / Outlook 导出 | ✅ | — | — | 手动上传 |
| Notion 导出 | — | ✅ | — | HTML 或 Markdown 导出 |
| Confluence 导出 | — | ✅ | — | HTML 导出或压缩包 |
| JIRA CSV / Linear JSON | — | — | ✅ | 项目跟踪导出 |
| PDF | — | ✅ | — | 手动上传 |
| 图片 / 截图 | ✅ | — | — | 手动上传 |
| Markdown / Text | ✅ | ✅ | — | 手动上传 |
| 直接粘贴文本 | ✅ | — | — | 复制粘贴任何内容 |

---

## 平台

### [Claude Code](https://claude.ai/code)
Anthropic 官方 Claude CLI。将此 Skill 安装到 `.claude/skills/` 目录，使用 `/create-teammate` 调用。

### [OpenClaw](https://openclaw.ai) 🦞
由 [@steipete](https://github.com/steipete) 开发的开源个人 AI 助手。运行在你自己的设备上，支持 25+ 个渠道（WhatsApp、Telegram、Slack、Discord、Teams、Signal、iMessage 等）。本地优先网关、持久记忆、语音、画布、定时任务，以及不断壮大的 Skill 生态。[GitHub](https://github.com/openclaw/openclaw)

### 🏆 [MyClaw.ai](https://myclaw.ai)
OpenClaw 托管服务——免去 Docker、服务器和配置的烦恼。一键部署、永远在线、自动更新、每日备份。几分钟内即可上线你的 OpenClaw 实例。如果你想让 teammate.skill 7×24 运行而无需自建服务器，这就是最佳选择。

---

## 安装

此 Skill 遵循 [AgentSkills](https://agentskills.io) 开放标准，兼容任何支持该标准的 Agent。

### Claude Code

```bash
# 项目级别（在 git 仓库根目录）
mkdir -p .claude/skills
git clone https://github.com/LeoYeAI/teammate-skill .claude/skills/create-teammate

# 全局（所有项目）
git clone https://github.com/LeoYeAI/teammate-skill ~/.claude/skills/create-teammate
```

### OpenClaw

```bash
git clone https://github.com/LeoYeAI/teammate-skill ~/.openclaw/workspace/skills/create-teammate
```

### 其他兼容 AgentSkills 的 Agent

克隆到你 Agent 的 Skill 目录。入口文件是带有标准 frontmatter 的 `SKILL.md`——任何支持 AgentSkills 格式的 Agent 都会自动识别。

### 依赖（可选）

```bash
pip3 install -r requirements.txt
```

> Slack 自动采集需要 Bot Token。GitHub 采集使用 `GITHUB_TOKEN`。详见 [INSTALL.md](INSTALL.md)。

---

## 使用方法

在你的 Agent（Claude Code、OpenClaw 或任何兼容 AgentSkills 的 Agent）中输入：

```
/create-teammate
```

按提示操作：输入名字、角色信息（如 `Google L5 backend engineer`）、性格标签，然后选择数据源。除了名字之外都可以跳过——即使只有描述也能生成有用的 Skill。

创建完成后，使用 `/{slug}` 调用该队友。

### 命令

| 命令 | 描述 |
|------|------|
| `/create-teammate` | 创建新的队友 Skill |
| `/list-teammates` | 列出所有队友 Skill |
| `/{slug}` | 调用完整 Skill（人格 + 工作能力） |
| `/{slug}-work` | 仅工作能力 |
| `/{slug}-persona` | 仅人格 |
| `/compare {a} vs {b}` | 并排对比及场景模拟 |
| `/export-teammate {slug}` | 导出可移植的 `.tar.gz` 包用于分享 |
| `/update-teammate {slug}` | 向现有队友追加新材料 |
| `/teammate-rollback {slug} {version}` | 回滚到之前的版本 |
| `/delete-teammate {slug}` | 删除队友 Skill |

---

## 演示

> 输入：`Stripe L3 backend engineer, INTJ, perfectionist, Stripe-style, brutal code reviewer`

**场景 1：代码审查**

```
User              ❯ Can you review this API endpoint?

teammate.skill    ❯ What problem does this actually solve? The PR description
                    doesn't say. Adding that first.
                    
                    Looking at the code: you're using float for the amount
                    field. That's a blocking issue — use Decimal for financial
                    values. Also, this endpoint isn't idempotent. What happens
                    on retry?
```

**场景 2：设计讨论**

```
User              ❯ Should we use MongoDB for this new feature?

teammate.skill    ❯ Strong disagree. We need ACID transactions for payment
                    flows. Mongo doesn't give us that. Let's stick with
                    Postgres. If the concern is schema flexibility, we can
                    use JSONB columns.
```

**场景 3：拒绝妥协**

```
User              ❯ Can we skip tests and ship this by Friday?

teammate.skill    ❯ No. We get the tests right or we don't ship. If Friday
                    is a hard deadline, let's cut scope instead of cutting
                    quality. What's the minimum we need for launch?
```

---

## 功能特性

### 生成的 Skill 结构

每个队友 Skill 由两部分组成，协同工作：

| 部分 | 内容 |
|------|------|
| **Part A — 工作能力** | 负责的系统、技术标准、工作流程、CR 重点、经验 |
| **Part B — 人格** | 5 层性格模型：硬性规则 → 身份认同 → 表达方式 → 决策倾向 → 人际互动 |

执行流程：`接收任务 → 人格决定态度 → 工作能力执行 → 以他们的语气输出`

### 支持的标签

**性格**：Meticulous · Good-enough · Blame-deflector · Perfectionist · Procrastinator · Ship-fast · Over-engineer · Scope-creeper · Bike-shedder · Micro-manager · Hands-off · Devil's-advocate · Mentor-type · Gatekeeper · Passive-aggressive · Confrontational …

**企业文化**：Google-style · Meta-style · Amazon-style · Apple-style · Stripe-style · Netflix-style · Microsoft-style · Startup-mode · Agency-mode · First-principles · Open-source-native

**级别**：Google L3-L11 · Meta E3-E9 · Amazon L4-L10 · Stripe L1-L5 · Microsoft 59-67+ · Apple ICT2-ICT6 · Netflix · Uber · Airbnb · ByteDance · Alibaba · Tencent · Generic (Junior/Senior/Staff/Principal)

### 进化

- **追加文件** → 自动分析增量 → 合并到相关章节，绝不覆盖已有结论
- **对话纠正** → 说"他们不会这样做，他们会……" → 写入纠正层，立即生效
- **版本控制** → 每次更新自动存档，可回滚到任何历史版本

---

## 质量保障

每个队友在交付前都会经过 **3 层质量管线**：

### 1. 质量门禁（预览前）
根据 7 条硬性规则验证生成内容：Layer 0 具体性、示例数量、口头禅密度、优先级排序、范围定义、无通用填充、标签→规则完整性。不合格项会在你看到预览之前自动修复。

### 2. 冒烟测试（创建后）
三个自动化测试提示针对每个生成的 Skill 运行：
- **领域问题** — Skill 是否使用真实系统/工具，而非泛泛建议？
- **施压场景** — 人格在压力下是否保持一致，还是退化为通用 AI？
- **超范围问题** — Skill 是否以本人风格承认知识边界？

```
🧪 Smoke Test: ✅ Domain ✅ Pushback ✅ Out-of-scope — 3/3 passed
```

### 3. 隐私扫描（导出前）
自动检测邮箱、电话号码、API Token、社会安全号码及其他个人身份信息：
```bash
python3 tools/privacy_guard.py --scan teammates/alex-chen/          # 检测
python3 tools/privacy_guard.py --scan teammates/alex-chen/ --redact  # 自动修复
```

原始知识文件（`knowledge/`）默认不会被纳入 git 和导出。

---

## 队友对比

并排对比及场景模拟：

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

还支持 **决策模拟** — 观看两个队友以本人风格就技术决策展开辩论。

---

## 导出与分享

将队友导出为可移植包：

```bash
/export-teammate alex-chen
# → alex-chen.teammate.tar.gz（仅 Skill 文件，不含原始数据）

# 在另一台机器上导入：
tar xzf alex-chen.teammate.tar.gz -C ./teammates/
```

导出包含：SKILL.md、work.md、persona.md、meta.json、版本历史和清单文件。
原始知识文件默认不包含 — 如需包含请添加 `--include-knowledge`（⚠️ 包含个人身份信息）。

---

## 项目结构

本项目遵循 [AgentSkills](https://agentskills.io) 开放标准：

```
create-teammate/
├── SKILL.md                  # Skill 入口文件
├── prompts/                  # 提示词模板
│   ├── intake.md             #   信息收集（3 个问题）
│   ├── work_analyzer.md      #   工作能力提取
│   ├── persona_analyzer.md   #   性格提取 + 标签翻译
│   ├── work_builder.md       #   work.md 生成模板
│   ├── persona_builder.md    #   persona.md 5 层结构
│   ├── merger.md             #   增量合并逻辑
│   ├── correction_handler.md #   对话纠正处理器
│   ├── compare.md            #   并排队友对比
│   └── smoke_test.md         #   创建后质量验证
├── tools/                    # 数据采集 & 管理
│   ├── slack_collector.py    #   Slack 自动采集器（Bot Token）
│   ├── slack_parser.py       #   Slack 导出 JSON 解析器
│   ├── github_collector.py   #   GitHub PR/Review 采集器
│   ├── teams_parser.py       #   Teams/Outlook 解析器
│   ├── email_parser.py       #   Gmail .mbox/.eml 解析器
│   ├── notion_parser.py      #   Notion 导出解析器
│   ├── confluence_parser.py  #   Confluence 导出解析器
│   ├── project_tracker_parser.py # JIRA/Linear 解析器
│   ├── skill_writer.py       #   Skill 文件管理
│   ├── version_manager.py    #   版本存档 & 回滚
│   ├── privacy_guard.py      #   PII 扫描器 & 自动脱敏
│   └── export.py             #   可移植包导出/导入
├── teammates/                # 生成的队友 Skill
│   └── example_alex/         #   示例：Stripe L3 后端工程师
├── docs/
├── requirements.txt
├── INSTALL.md
└── LICENSE
```

---

## 最佳实践

- **源材料质量 = Skill 质量**：真实聊天记录 + 设计文档 > 纯手动描述
- 优先采集：**他们撰写的设计文档** > **代码审查评论** > **决策讨论** > 闲聊
- GitHub PR 和 Review 是工作能力的金矿——它们揭示了真实的编码标准和审查重点
- Slack 对话是人格的金矿——它们展示了不同压力下的沟通风格
- 先从手动描述开始，然后在找到真实数据后逐步追加

---

## 许可证

MIT License — 详见 [LICENSE](LICENSE)。

---

<div align="center">

**teammate.skill** — 因为最好的知识传承不是一份文档，而是一个可运行的模型。

</div>
