[English](README.md) | [简体中文](README.zh-CN.md) | [Français](README.fr.md) | [Deutsch](README.de.md) | [Русский](README.ru.md) | [日本語](README.ja.md) | [Italiano](README.it.md) | [Español](README.es.md)

<div align="center">

<h1><img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=50&duration=3000&pause=1000&color=6C63FF&center=true&vCenter=true&width=600&height=80&lines=teammate.skill" alt="teammate.skill" /></h1>

> *チームメイトは去った。でも、そのコンテキストまで失う必要はなかった。*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://python.org)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet)](https://claude.ai/code)
[![OpenClaw](https://img.shields.io/badge/OpenClaw-Skill-orange)](https://openclaw.ai)
[![AgentSkills](https://img.shields.io/badge/AgentSkills-Standard-green)](https://agentskills.io)

<br>

チームメイトが退職して、メンテナンスされないドキュメントの山が残された？<br>
シニアエンジニアが辞めて、暗黙知がすべて消えた？<br>
メンターが異動して、3年分のコンテキストが一夜で蒸発した？<br>
共同創業者が新しい役職に移り、引き継ぎ資料はたった2ページ？<br>

**退職をスキルという永続資産に変えよう。ナレッジの不死化へようこそ。**

<br>

ソース資料（Slackメッセージ、GitHub PR、メール、Notionドキュメント、議事録）と<br>
その人物の説明を提供するだけで<br>
**本人のように機能するAIスキル**が生成されます<br>
— 本人のスタイルでコードを書き、本人の基準でPRをレビューし、本人の声で質問に答えます

[対応データソース](#対応データソース) · [インストール](#インストール) · [使い方](#使い方) · [デモ](#デモ) · [詳細インストールガイド](INSTALL.md)

</div>

---

## 対応データソース

> ベータ版 — さらに多くの連携を追加予定！

| ソース | メッセージ | ドキュメント / Wiki | コード & PR | 備考 |
|--------|:--------:|:-----------:|:----------:|-------|
| Slack（自動収集） | ✅ API | — | — | ユーザー名を入力するだけで全自動 |
| GitHub（自動収集） | — | — | ✅ API | PR、レビュー、Issueコメント |
| Slack export JSON | ✅ | — | — | 手動アップロード |
| Gmail `.mbox` / `.eml` | ✅ | — | — | 手動アップロード |
| Teams / Outlook export | ✅ | — | — | 手動アップロード |
| Notion export | — | ✅ | — | HTML または Markdown エクスポート |
| Confluence export | — | ✅ | — | HTML エクスポートまたは zip |
| JIRA CSV / Linear JSON | — | — | ✅ | 課題管理ツールのエクスポート |
| PDF | — | ✅ | — | 手動アップロード |
| 画像 / スクリーンショット | ✅ | — | — | 手動アップロード |
| Markdown / Text | ✅ | ✅ | — | 手動アップロード |
| テキスト直接貼り付け | ✅ | — | — | 何でもコピー＆ペースト |

---

## プラットフォーム

### [Claude Code](https://claude.ai/code)
Anthropic公式のClaude CLI。`.claude/skills/` にこのスキルをインストールし、`/create-teammate` で起動します。

### 🦞 [OpenClaw](https://openclaw.ai)
[@steipete](https://github.com/steipete) によるオープンソースのパーソナルAIアシスタント。自分のデバイスで動作し、25以上のチャネル（WhatsApp、Telegram、Slack、Discord、Teams、Signal、iMessageなど）で応答。ローカルファーストのゲートウェイ、永続メモリ、音声、キャンバス、cronジョブ、成長中のスキルエコシステム。[GitHub](https://github.com/openclaw/openclaw)

### 🏆 [MyClaw.ai](https://myclaw.ai)
OpenClawのマネージドホスティング — Docker、サーバー、設定作業は不要。ワンクリックデプロイ、常時稼働、自動アップデート、毎日バックアップ。数分でOpenClawインスタンスが稼働開始。セルフホスティングなしでteammate.skillを24時間365日運用したい方に最適。

---

## インストール

このスキルは [AgentSkills](https://agentskills.io) オープンスタンダードに準拠しており、互換性のあるすべてのエージェントで動作します。

### Claude Code

```bash
# プロジェクト単位（gitリポジトリのルートで実行）
mkdir -p .claude/skills
git clone https://github.com/LeoYeAI/teammate-skill .claude/skills/create-teammate

# グローバル（全プロジェクト共通）
git clone https://github.com/LeoYeAI/teammate-skill ~/.claude/skills/create-teammate
```

### OpenClaw

```bash
git clone https://github.com/LeoYeAI/teammate-skill ~/.openclaw/workspace/skills/create-teammate
```

### その他の AgentSkills 互換エージェント

エージェントのスキルディレクトリにクローンしてください。エントリポイントは標準フロントマター付きの `SKILL.md` です。AgentSkills フォーマットを読み取れるエージェントであれば自動的に認識されます。

### 依存関係（オプション）

```bash
pip3 install -r requirements.txt
```

> Slack自動収集にはBot Tokenが必要です。GitHub収集には `GITHUB_TOKEN` を使用します。詳細は [INSTALL.md](INSTALL.md) を参照してください。

---

## 使い方

エージェント（Claude Code、OpenClaw、またはその他のAgentSkills互換エージェント）で以下を入力します：

```
/create-teammate
```

プロンプトに従って進めます：名前、役職情報（例：`Google L5 backend engineer`）、パーソナリティタグを入力し、データソースを選択します。名前以外はすべてスキップ可能で、説明文だけでも実用的なスキルが生成されます。

作成後は `/{slug}` でチームメイトを呼び出せます。

### コマンド一覧

| コマンド | 説明 |
|---------|-------------|
| `/create-teammate` | 新しいチームメイトスキルを作成 |
| `/list-teammates` | すべてのチームメイトスキルを一覧表示 |
| `/{slug}` | フルスキルを呼び出し（ペルソナ＋ワーク） |
| `/{slug}-work` | ワーク機能のみ |
| `/{slug}-persona` | ペルソナのみ |
| `/compare {a} vs {b}` | サイドバイサイド比較とシナリオシミュレーション |
| `/export-teammate {slug}` | 共有用のポータブル `.tar.gz` パッケージをエクスポート |
| `/update-teammate {slug}` | 既存のチームメイトに新しい資料を追加 |
| `/teammate-rollback {slug} {version}` | 以前のバージョンにロールバック |
| `/delete-teammate {slug}` | チームメイトスキルを削除 |

---

## デモ

> 入力例: `Stripe L3 backend engineer, INTJ, perfectionist, Stripe-style, brutal code reviewer`

**シナリオ 1: コードレビュー**

```
User              ❯ Can you review this API endpoint?

teammate.skill    ❯ What problem does this actually solve? The PR description
                    doesn't say. Adding that first.
                    
                    Looking at the code: you're using float for the amount
                    field. That's a blocking issue — use Decimal for financial
                    values. Also, this endpoint isn't idempotent. What happens
                    on retry?
```

**シナリオ 2: 設計ディスカッション**

```
User              ❯ Should we use MongoDB for this new feature?

teammate.skill    ❯ Strong disagree. We need ACID transactions for payment
                    flows. Mongo doesn't give us that. Let's stick with
                    Postgres. If the concern is schema flexibility, we can
                    use JSONB columns.
```

**シナリオ 3: 反論・プッシュバック**

```
User              ❯ Can we skip tests and ship this by Friday?

teammate.skill    ❯ No. We get the tests right or we don't ship. If Friday
                    is a hard deadline, let's cut scope instead of cutting
                    quality. What's the minimum we need for launch?
```

---

## 機能

### 生成されるスキルの構造

各チームメイトスキルは連携して動作する2つのパートで構成されます：

| パート | 内容 |
|------|---------|
| **Part A — Work Skill** | 担当システム、技術標準、ワークフロー、コードレビュー重視点、経験 |
| **Part B — Persona** | 5層のパーソナリティ：ハードルール → アイデンティティ → 表現 → 意思決定 → 対人関係 |

実行フロー: `タスク受信 → ペルソナが姿勢を決定 → Work Skillが実行 → 本人の声でアウトプット`

### 対応タグ

**パーソナリティ**: Meticulous · Good-enough · Blame-deflector · Perfectionist · Procrastinator · Ship-fast · Over-engineer · Scope-creeper · Bike-shedder · Micro-manager · Hands-off · Devil's-advocate · Mentor-type · Gatekeeper · Passive-aggressive · Confrontational …

**企業カルチャー**: Google-style · Meta-style · Amazon-style · Apple-style · Stripe-style · Netflix-style · Microsoft-style · Startup-mode · Agency-mode · First-principles · Open-source-native

**レベル**: Google L3-L11 · Meta E3-E9 · Amazon L4-L10 · Stripe L1-L5 · Microsoft 59-67+ · Apple ICT2-ICT6 · Netflix · Uber · Airbnb · ByteDance · Alibaba · Tencent · Generic (Junior/Senior/Staff/Principal)

### 進化機能

- **ファイル追加** → 差分を自動解析 → 関連セクションにマージ、既存の結論は上書きしない
- **会話による修正** → 「あの人はそうしない、こうする…」と伝えるだけ → 修正レイヤーに書き込まれ、即座に反映
- **バージョン管理** → 更新ごとに自動アーカイブ、任意の過去バージョンにロールバック可能

---

## 品質保証

すべてのチームメイトは、あなたに届く前に **3層の品質パイプライン** を通過します：

### 1. 品質ゲート（プレビュー前）
生成されたコンテンツを7つの厳格なルールで検証：Layer 0の具体性、例の数、口癖の密度、優先順位の順序、スコープ定義、汎用的なフィラーの排除、タグ→ルールの完全性。不合格項目はプレビューが表示される前に自動修正されます。

### 2. スモークテスト（作成後）
3つの自動テストプロンプトが各生成スキルに対して実行されます：
- **ドメイン質問** — スキルが汎用的なアドバイスではなく、実際のシステム/ツールを使用しているか？
- **プレッシャーシナリオ** — ペルソナが圧力下でも維持されるか、それとも汎用AIに崩壊するか？
- **スコープ外質問** — スキルがキャラクターを保ちながら知識の限界を認めるか？

```
🧪 Smoke Test: ✅ Domain ✅ Pushback ✅ Out-of-scope — 3/3 passed
```

### 3. プライバシースキャン（エクスポート前）
メールアドレス、電話番号、APIトークン、SSN、その他の個人情報を自動検出：
```bash
python3 tools/privacy_guard.py --scan teammates/alex-chen/          # 検出
python3 tools/privacy_guard.py --scan teammates/alex-chen/ --redact  # 自動修正
```

生の知識ファイル（`knowledge/`）はデフォルトでgitとエクスポートから除外されます。

---

## チームメイトの比較

サイドバイサイド比較とシナリオシミュレーション：

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

**意思決定シミュレーション** もサポート — 2人のチームメイトがキャラクターを保ちながら技術的な決定について議論する様子を観察できます。

---

## エクスポート＆共有

チームメイトをポータブルパッケージとしてエクスポート：

```bash
/export-teammate alex-chen
# → alex-chen.teammate.tar.gz（スキルファイルのみ、生データなし）

# 別のマシンにインポート：
tar xzf alex-chen.teammate.tar.gz -C ./teammates/
```

エクスポートに含まれるもの：SKILL.md、work.md、persona.md、meta.json、バージョン履歴、マニフェスト。
生の知識ファイルはデフォルトで除外されます — 必要な場合は `--include-knowledge` を追加してください（⚠️ 個人情報を含みます）。

---

## プロジェクト構成

このプロジェクトは [AgentSkills](https://agentskills.io) オープンスタンダードに準拠しています：

```
create-teammate/
├── SKILL.md                  # スキルのエントリポイント
├── prompts/                  # プロンプトテンプレート
│   ├── intake.md             #   情報収集（3つの質問）
│   ├── work_analyzer.md      #   ワーク能力の抽出
│   ├── persona_analyzer.md   #   パーソナリティ抽出 + タグ変換
│   ├── work_builder.md       #   work.md 生成テンプレート
│   ├── persona_builder.md    #   persona.md 5層構造
│   ├── merger.md             #   差分マージロジック
│   ├── correction_handler.md #   会話修正ハンドラー
│   ├── compare.md            #   チームメイトのサイドバイサイド比較
│   └── smoke_test.md         #   作成後の品質検証
├── tools/                    # データ収集 & 管理ツール
│   ├── slack_collector.py    #   Slack自動収集（Bot Token）
│   ├── slack_parser.py       #   Slack export JSONパーサー
│   ├── github_collector.py   #   GitHub PR/レビュー収集
│   ├── teams_parser.py       #   Teams/Outlookパーサー
│   ├── email_parser.py       #   Gmail .mbox/.eml パーサー
│   ├── notion_parser.py      #   Notionエクスポートパーサー
│   ├── confluence_parser.py  #   Confluenceエクスポートパーサー
│   ├── project_tracker_parser.py # JIRA/Linearパーサー
│   ├── skill_writer.py       #   スキルファイル管理
│   ├── version_manager.py    #   バージョンアーカイブ & ロールバック
│   ├── privacy_guard.py      #   PIIスキャナー & 自動マスキング
│   └── export.py             #   ポータブルパッケージのエクスポート/インポート
├── teammates/                # 生成されたチームメイトスキル
│   └── example_alex/         #   例: Stripe L3 backend engineer
├── docs/
├── requirements.txt
├── INSTALL.md
└── LICENSE
```

---

## ベストプラクティス

- **ソース資料の質 = スキルの質**：実際のチャットログ + 設計ドキュメント > 手動の説明文のみ
- 収集の優先順位：**本人が書いた設計ドキュメント** > **コードレビューコメント** > **意思決定の議論** > 雑談
- GitHub PRとレビューはWork Skillの宝庫 — 実際のコーディング規約やレビューの重視点が明らかになります
- SlackスレッドはPersonaの宝庫 — 様々なプレッシャー下でのコミュニケーションスタイルが見えてきます
- まず手動の説明文から始めて、実データが見つかり次第、段階的に追加していくのがおすすめです

---

## ライセンス

MIT License — 詳細は [LICENSE](LICENSE) をご覧ください。

---

<div align="center">

**teammate.skill** — 最高のナレッジ移転はドキュメントではなく、動くモデルだから。

</div>
