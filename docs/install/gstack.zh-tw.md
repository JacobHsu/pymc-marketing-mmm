# gstack

> 「自從去年十二月以來，我幾乎沒有自己打過一行程式碼，這是個極大的轉變。」— [Andrej Karpathy](https://fortune.com/2026/03/21/andrej-karpathy-openai-cofounder-ai-agents-coding-state-of-psychosis-openclaw/)，No Priors podcast，2026 年 3 月

聽到 Karpathy 說這句話，我想知道他是怎麼做到的。一個人如何做到二十人團隊的產出？Peter Steinberger 幾乎靠一己之力，借助 AI agents 打造出 [OpenClaw](https://github.com/openclaw/openclaw)（GitHub 247K stars）。革命已經到來。一個有正確工具的獨立開發者，可以比傳統團隊移動得更快。

我是 [Garry Tan](https://x.com/garrytan)，[Y Combinator](https://www.ycombinator.com/) 的 President & CEO。我和數千家新創合作過——Coinbase、Instacart、Rippling——在它們還只是車庫裡一兩個人的時候。加入 YC 之前，我是 Palantir 最早的工程師/PM/設計師之一，共同創辦了 Posterous（後來賣給 Twitter），並打造了 YC 內部社交網路 Bookface。

**gstack 是我的答案。** 我做了二十年的產品，而現在我的出貨量超過以往任何時候。過去 60 天：3 個生產服務、40+ 個已上線功能，兼職完成，同時全職主持 YC。以邏輯程式碼變更計算（而非 AI 會虛增的原始 LOC），我 2026 年的速率是 **2013 年的約 810 倍**（每天 11,417 對 14 行邏輯程式碼）。從年初到 4 月 18 日，2026 年的產出已經是整個 2013 年的 **240 倍**。計算範圍涵蓋 40 個公開和私有的 `garrytan/*` repo（包含 Bookface），排除一個 demo repo 後統計。AI 寫了其中大部分。重點不是誰打的字，而是交付了什麼。

> 批評 LOC 的人說 AI 會虛增行數，這沒錯。但他們說標準化通膨後我的生產力反而更低，這是錯的。我的生產力更高，而且高出很多。完整方法論、注意事項和重現腳本：**[關於 LOC 爭議](docs/ON_THE_LOC_CONTROVERSY.md)**。

**2026 — 1,237 次貢獻（持續增加中）：**

![GitHub 貢獻 2026 — 1,237 次貢獻，1-3 月大幅加速](docs/images/github-2026.png)

**2013 — 在 YC 打造 Bookface 時（772 次貢獻）：**

![GitHub 貢獻 2013 — 772 次貢獻，在 YC 打造 Bookface](docs/images/github-2013.png)

同一個人。不同的時代。差異在於工具。

**gstack 就是我的做法。** 它把 Claude Code 變成一個虛擬工程團隊——一位重新思考產品的 CEO、一位鎖定架構的工程主管、一位抓出 AI 爛設計的設計師、一位找出生產 bug 的審查者、一位開真實瀏覽器的 QA 主管、一位執行 OWASP + STRIDE 審計的資安長，以及一位負責出貨 PR 的發版工程師。二十三位專業角色和八個強力工具，全是 slash 指令，全是 Markdown，全部免費，MIT 授權。

這是我的開源軟體工廠。我每天都在用。我分享出來，是因為這些工具應該讓所有人都能取得。

Fork 它、改進它、讓它成為你的。如果你想批評免費開源軟體——歡迎，但我寧願你先試試看。

**適合對象：**
- **創辦人和 CEO** — 尤其是仍然想親自出貨的技術型創辦人
- **第一次使用 Claude Code 的人** — 有結構化角色，不用面對空白提示詞
- **技術主管和資深工程師** — 每個 PR 都有嚴謹的審查、QA 和發版自動化

## 快速開始

1. 安裝 gstack（30 秒，見下文）
2. 執行 `/office-hours` — 描述你在做什麼
3. 對任何功能想法執行 `/plan-ceo-review`
4. 對任何有改動的分支執行 `/review`
5. 對你的 staging URL 執行 `/qa`
6. 停在這裡。你自然會知道這是不是你要的東西。

## 安裝 — 30 秒

**需求：** [Claude Code](https://docs.anthropic.com/en/docs/claude-code)、[Git](https://git-scm.com/)、[Bun](https://bun.sh/) v1.0+、[Node.js](https://nodejs.org/)（僅 Windows 需要）

### 步驟一：安裝到你的機器

打開 Claude Code，貼上以下指令。Claude 會處理其餘的事。

> Install gstack: run **`git clone --single-branch --depth 1 https://github.com/garrytan/gstack.git ~/.claude/skills/gstack && cd ~/.claude/skills/gstack && ./setup`** then add a "gstack" section to CLAUDE.md that says to use the /browse skill from gstack for all web browsing, never use mcp\_\_claude-in-chrome\_\_\* tools, and lists the available skills: /office-hours, /plan-ceo-review, /plan-eng-review, /plan-design-review, /design-consultation, /design-shotgun, /design-html, /review, /ship, /land-and-deploy, /canary, /benchmark, /browse, /connect-chrome, /qa, /qa-only, /design-review, /setup-browser-cookies, /setup-deploy, /setup-gbrain, /retro, /investigate, /document-release, /codex, /cso, /autoplan, /plan-devex-review, /devex-review, /careful, /freeze, /guard, /unfreeze, /gstack-upgrade, /learn. Then ask the user if they also want to add gstack to the current project so teammates get it.

### 步驟二：團隊模式 — 共享 repo 自動更新（推薦）

在你的 repo 內貼上以下指令。它會切換到團隊模式、初始化 repo 讓隊友自動取得 gstack，並提交變更：

```bash
(cd ~/.claude/skills/gstack && ./setup --team) && ~/.claude/skills/gstack/bin/gstack-team-init required && git add .claude/ CLAUDE.md && git commit -m "require gstack for AI-assisted work"
```

repo 裡沒有 vendor 檔案、沒有版本漂移、不用手動升級。每個 Claude Code session 啟動時都會做一次快速的自動更新檢查（節流為每小時一次，網路失敗時安全跳過，完全靜默）。

把 `required` 換成 `optional` 可以改為提示隊友而非強制要求。

### OpenClaw

OpenClaw 透過 ACP 啟動 Claude Code session，因此當 Claude Code 安裝了 gstack，所有 gstack skill 都能直接使用。貼上以下指令給你的 OpenClaw agent：

> Install gstack: run `git clone --single-branch --depth 1 https://github.com/garrytan/gstack.git ~/.claude/skills/gstack && cd ~/.claude/skills/gstack && ./setup` to install gstack for Claude Code. Then add a "Coding Tasks" section to AGENTS.md that says: when spawning Claude Code sessions for coding work, tell the session to use gstack skills. Include these examples — security audit: "Load gstack. Run /cso", code review: "Load gstack. Run /review", QA test a URL: "Load gstack. Run /qa https://...", build a feature end-to-end: "Load gstack. Run /autoplan, implement the plan, then run /ship", plan before building: "Load gstack. Run /office-hours then /autoplan. Save the plan, don't implement."

**設定後，只要自然地和你的 OpenClaw agent 說話：**

| 你說的 | 會發生什麼 |
|--------|-----------|
| "修正 README 裡的錯字" | 簡單任務 — Claude Code session，不需要 gstack |
| "對這個 repo 做資安審計" | 啟動 Claude Code 並執行 `Run /cso` |
| "幫我做一個通知功能" | 啟動 Claude Code 執行 /autoplan → 實作 → /ship |
| "幫我規劃 v2 API 重設計" | 啟動 Claude Code 執行 /office-hours → /autoplan，儲存計畫 |

進階排程路由和 gstack-lite/gstack-full 提示模板請參考 [docs/OPENCLAW.md](docs/OPENCLAW.md)。

### 原生 OpenClaw Skills（透過 ClawHub）

四個方法論 skill，直接在你的 OpenClaw agent 中運作，不需要 Claude Code session。從 ClawHub 安裝：

```
clawhub install gstack-openclaw-office-hours gstack-openclaw-ceo-review gstack-openclaw-investigate gstack-openclaw-retro
```

| Skill | 功能 |
|-------|------|
| `gstack-openclaw-office-hours` | 產品審問，6 個強迫思考問題 |
| `gstack-openclaw-ceo-review` | 策略挑戰，4 種範圍模式 |
| `gstack-openclaw-investigate` | 根本原因除錯方法論 |
| `gstack-openclaw-retro` | 每週工程回顧 |

這些是對話式 skill，你的 OpenClaw agent 直接透過聊天執行它們。

### 其他 AI Agents

gstack 支援 10 種 AI coding agent，不只是 Claude。安裝時會自動偵測你安裝了哪些 agent：

```bash
git clone --single-branch --depth 1 https://github.com/garrytan/gstack.git ~/gstack
cd ~/gstack && ./setup
```

或用 `./setup --host <name>` 指定特定 agent：

| Agent | 旗標 | Skills 安裝位置 |
|-------|------|----------------|
| OpenAI Codex CLI | `--host codex` | `~/.codex/skills/gstack-*/` |
| OpenCode | `--host opencode` | `~/.config/opencode/skills/gstack-*/` |
| Cursor | `--host cursor` | `~/.cursor/skills/gstack-*/` |
| Factory Droid | `--host factory` | `~/.factory/skills/gstack-*/` |
| Slate | `--host slate` | `~/.slate/skills/gstack-*/` |
| Kiro | `--host kiro` | `~/.kiro/skills/gstack-*/` |
| Hermes | `--host hermes` | `~/.hermes/skills/gstack-*/` |
| GBrain (mod) | `--host gbrain` | `~/.gbrain/skills/gstack-*/` |

**想新增對其他 agent 的支援？** 參考 [docs/ADDING_A_HOST.md](docs/ADDING_A_HOST.md)。只需要一個 TypeScript 設定檔，不用改任何程式碼。

## 看它如何運作

```
你：    我想做一個每日行事曆摘要 app。
你：    /office-hours
Claude：[問你的痛點 — 具體案例，不是假設情境]

你：    多個 Google 行事曆、活動資訊過時、地點錯誤。
        準備工作耗時很長，結果還是不夠好……

Claude：我要挑戰你的框架。你說的是「每日摘要 app」，
        但你實際描述的是一個個人 AI 幕僚長。
        [提取 5 個你沒意識到自己在描述的能力]
        [挑戰 4 個前提 — 你同意、不同意，或調整]
        [產出 3 個實作方向，附上工作量估算]
        建議：明天先出貨最小切入點，從實際使用中學習。
        完整願景是 3 個月的專案 — 先把那個真正有用的
        每日摘要做出來。
        [撰寫設計文件 → 自動流入下游 skill]

你：    /plan-ceo-review
        [讀取設計文件，挑戰範圍，執行 10 節審查]

你：    /plan-eng-review
        [資料流、狀態機、錯誤路徑的 ASCII 圖表]
        [測試矩陣、失敗模式、安全疑慮]

你：    Approve plan. Exit plan mode.
        [在 11 個檔案裡寫了 2,400 行。約 8 分鐘。]

你：    /review
        [已自動修復] 2 個問題。[需確認] Race condition → 你核准修復。

你：    /qa https://staging.myapp.com
        [開啟真實瀏覽器，點擊流程，找到並修復一個 bug]

你：    /ship
        測試：42 → 51（+9 個新測試）。PR：github.com/you/app/pull/42
```

你說的是「每日摘要 app」。Agent 說「你在建的是 AI 幕僚長」— 因為它聽的是你的痛，不是你的功能請求。八個指令，從頭到尾。這不是 copilot，這是一個團隊。

## 衝刺流程

gstack 是一個流程，不只是一堆工具的集合。skill 的執行順序就是一個衝刺的執行順序：

**思考 → 規劃 → 建造 → 審查 → 測試 → 出貨 → 回顧**

每個 skill 都會帶入下一個。`/office-hours` 寫的設計文件會被 `/plan-ceo-review` 讀取。`/plan-eng-review` 寫的測試計畫會被 `/qa` 拿來用。`/review` 抓到的 bug，`/ship` 會確認已修復。沒有任何事情會漏掉，因為每個步驟都知道前一步做了什麼。

| Skill | 你的專業角色 | 他們做什麼 |
|-------|------------|-----------|
| `/office-hours` | **YC Office Hours** | 從這裡開始。六個強迫思考問題，在你寫程式之前重新框架你的產品。挑戰你的框架、質疑前提、產出實作替代方案。設計文件會流入所有下游 skill。|
| `/plan-ceo-review` | **CEO / 創辦人** | 重新思考問題。找出請求裡隱藏的 10 星產品。四種模式：擴展、選擇性擴展、維持範圍、縮減。|
| `/plan-eng-review` | **工程主管** | 鎖定架構、資料流、圖表、邊緣案例和測試。把隱藏的假設逼出來攤在陽光下。|
| `/plan-design-review` | **資深設計師** | 為每個設計維度評分 0-10，解釋 10 分的樣子，然後編輯計畫以達到那個水準。AI 爛設計偵測。互動式 — 每個設計決策一個 AskUserQuestion。|
| `/plan-devex-review` | **開發體驗主管** | 互動式 DX 審查：探索開發者角色、對比競爭對手的 TTHW、設計你的魔法時刻、逐步追蹤摩擦點。三種模式：DX 擴展、DX 打磨、DX 分流。20-45 個強迫思考問題。|
| `/design-consultation` | **設計夥伴** | 從零打造完整的設計系統。研究現有方案，提出創意風險，生成真實感的產品 mockup。|
| `/review` | **資深工程師** | 找出通過 CI 但在生產環境爆炸的 bug。自動修復顯而易見的問題。標記完整性缺口。|
| `/investigate` | **除錯專家** | 系統化的根本原因除錯。鐵律：沒有調查就沒有修復。追蹤資料流、測試假設，3 次修復失敗後停止。|
| `/design-review` | **會寫程式的設計師** | 和 /plan-design-review 一樣的審計，然後修復發現的問題。Atomic commits，前後截圖對比。|
| `/devex-review` | **DX 測試者** | 即時開發體驗審計。實際測試你的 onboarding：導航文件、嘗試入門流程、計時 TTHW、對錯誤截圖。對比 `/plan-devex-review` 的分數 — 這是回飛鏢，告訴你計畫和現實是否相符。|
| `/design-shotgun` | **設計探索者** | 「讓我看看選項。」生成 4-6 個 AI mockup 變體，在瀏覽器裡開啟對比板，收集你的回饋，然後迭代。品味記憶學習你喜歡什麼。重複直到你喜歡某個方向，然後交給 `/design-html`。|
| `/design-html` | **設計工程師** | 把 mockup 轉成真正可用的生產級 HTML。預計算排版：文字在縮放時正確換行、高度根據內容調整、版型動態響應。30KB、零依賴。偵測 React/Svelte/Vue。依設計類型智慧路由 API（登陸頁 vs 儀表板 vs 表單）。輸出是可以真正上線的，不是 demo。|
| `/qa` | **QA 主管** | 測試你的 app、找到 bug、用 atomic commits 修復、重新驗證。為每個修復自動生成迴歸測試。|
| `/qa-only` | **QA 報告者** | 和 /qa 相同的方法論，但只報告。純粹的 bug 報告，不修改程式碼。|
| `/pair-agent` | **多 Agent 協調者** | 把你的瀏覽器分享給任何 AI agent。一個指令，一次貼上，就連接好了。支援 OpenClaw、Hermes、Codex、Cursor 或任何能執行 curl 的工具。每個 agent 有自己的分頁。自動啟動有界面的模式讓你看到一切。自動啟動 ngrok tunnel 給遠端 agent。範圍限制的 token、分頁隔離、速率限制、活動歸因。|
| `/cso` | **資安長** | OWASP Top 10 + STRIDE 威脅模型。零噪音：17 個誤報排除條件、8/10+ 信心門檻、獨立發現驗證。每個發現都包含具體的攻擊場景。|
| `/ship` | **發版工程師** | 同步 main、執行測試、審計覆蓋率、推送、開 PR。如果你沒有測試框架，從頭幫你建立。|
| `/land-and-deploy` | **發版工程師** | 合併 PR、等待 CI 和部署、驗證生產環境健康狀態。從「已核准」到「已驗證上線」，一個指令搞定。|
| `/canary` | **SRE** | 部署後監控循環。監看 console 錯誤、效能退化和頁面失敗。|
| `/benchmark` | **效能工程師** | 建立頁面載入時間、Core Web Vitals 和資源大小的基準。每個 PR 做前後對比。|
| `/document-release` | **技術寫作者** | 更新所有專案文件以符合你剛出貨的內容。自動找出過時的 README。|
| `/retro` | **工程主管** | 有感知的每週回顧。個人分解、出貨連勝、測試健康趨勢、成長機會。`/retro global` 跨所有專案和 AI 工具（Claude Code、Codex、Gemini）執行。|
| `/browse` | **QA 工程師** | 給 agent 一雙眼睛。真實的 Chromium 瀏覽器、真實的點擊、真實的截圖。每個指令約 100ms。`/open-gstack-browser` 啟動 GStack Browser，含側邊欄、反偵測隱身模式和自動模型路由。|
| `/setup-browser-cookies` | **Session 管理者** | 從你的真實瀏覽器（Chrome、Arc、Brave、Edge）匯入 cookies 到無頭 session。測試需要登入的頁面。|
| `/autoplan` | **審查流水線** | 一個指令，完整審查的計畫。自動依序執行 CEO → 設計 → 工程審查，內建決策原則。只把品味決策浮出讓你核准。|
| `/learn` | **記憶管理** | 管理 gstack 跨 session 學到的東西。審查、搜尋、修剪、匯出專案特定的模式、陷阱和偏好。學習會跨 session 累積，讓 gstack 在你的 codebase 上越來越聰明。|

### 我應該用哪種審查？

| 建造對象 | 規劃階段（寫程式前） | 即時審計（出貨後） |
|---------|-------------------|-----------------|
| **終端使用者**（UI、Web app、Mobile）| `/plan-design-review` | `/design-review` |
| **開發者**（API、CLI、SDK、文件）| `/plan-devex-review` | `/devex-review` |
| **架構**（資料流、效能、測試）| `/plan-eng-review` | `/review` |
| **以上全部** | `/autoplan`（自動執行 CEO → 設計 → 工程 → DX，自動偵測適用哪些）| — |

### 強力工具

| Skill | 功能 |
|-------|------|
| `/codex` | **第二意見** — 從 OpenAI Codex CLI 取得獨立的程式碼審查。三種模式：審查（通過/失敗門檻）、對抗性挑戰和開放諮詢。當 `/review`（Claude）和 `/codex`（OpenAI）都審查了同一分支後，提供跨模型分析。|
| `/careful` | **安全護欄** — 在任何破壞性指令前警告（rm -rf、DROP TABLE、force-push）。說「be careful」啟動。可以覆蓋任何警告。|
| `/freeze` | **編輯鎖定** — 限制只能編輯某個目錄。除錯時防止意外修改範圍外的程式碼。|
| `/guard` | **完整安全** — 一個指令同時啟動 `/careful` 和 `/freeze`。生產環境工作時的最高安全等級。|
| `/unfreeze` | **解鎖** — 移除 `/freeze` 設定的邊界。|
| `/open-gstack-browser` | **GStack 瀏覽器** — 啟動 GStack Browser，含側邊欄、反偵測隱身、自動模型路由（Sonnet 負責操作，Opus 負責分析）、一鍵 cookie 匯入和 Claude Code 整合。清理頁面、智慧截圖、編輯 CSS，並把資訊傳回終端。|
| `/setup-deploy` | **部署設定器** — 一次性設定 `/land-and-deploy`。偵測你的平台、生產環境 URL 和部署指令。|
| `/setup-gbrain` | **GBrain Onboarding** — 從零到 gbrain 跑起來，5 分鐘以內。PGLite 本地、Supabase 現有 URL，或透過 Management API 自動建立新的 Supabase 專案。為 Claude Code 和每個 repo 的信任三元組（讀寫/唯讀/拒絕）註冊 MCP。[完整指南](USING_GBRAIN_WITH_GSTACK.md)。|
| `/sync-gbrain` | **同步大腦** — 透過 `gbrain sources add` + `gbrain sync --strategy code` 把這個 repo 的程式碼重新索引到 gbrain，刷新 CLAUDE.md 裡的 `## GBrain Search Guidance` 區塊，並在能力檢查失敗時自動移除指引。支援 `--incremental`（預設）、`--full`、`--dry-run`。冪等，可安全重複執行。|
| `/gstack-upgrade` | **自我更新** — 升級 gstack 到最新版本。自動偵測全域安裝 vs vendor 安裝，同步兩者，顯示更新內容。|

### 新二進位程式（v0.19）

除了 slash-command skill，gstack 還提供獨立 CLI，用於不適合在 session 內執行的工作流程：

| 指令 | 功能 |
|------|------|
| `gstack-model-benchmark` | **跨模型基準測試** — 對 Claude、GPT（透過 Codex CLI）和 Gemini 執行相同的提示詞；比較延遲、token 用量、費用和（選擇性）LLM 評審品質分數。每個供應商的認證自動偵測，未安裝的供應商自動跳過。輸出為表格、JSON 或 Markdown。`--dry-run` 驗證旗標和認證但不消耗 API。|
| `gstack-taste-update` | **設計品味學習** — 把 `/design-shotgun` 的核准和拒絕記錄到每個專案持久化的品味檔案中。每週衰減 5%。回饋給未來的變體生成，讓系統學習你實際選擇什麼。|

### 連續存檔模式（選擇性啟用，預設本地）

設定 `gstack-config set checkpoint_mode continuous`，skill 就會在過程中自動以 `WIP:` 前綴提交你的工作，並附上結構化的 `[gstack-context]` 主體（決策、剩餘工作、失敗的嘗試）。能在崩潰和任務切換時存活。`/context-restore` 讀取這些提交以重建 session 狀態。`/ship` 在 PR 前過濾並壓縮 WIP 提交（保留非 WIP 提交），讓 bisect 保持乾淨。推送為選擇性，透過 `checkpoint_push=true` 啟用 — 預設只在本地，這樣不會在每次 WIP 提交時觸發 CI。

### 網域 skill 和原始 CDP 逃生艙

兩個新的瀏覽器原語讓 gstack agent 隨時間累積能力：

- **`$B domain-skill save`** — agent 儲存每個網站的筆記（例如「LinkedIn 的 Apply 按鈕在 iframe 裡」），下次訪問該域名時自動觸發。隔離 → 3 次成功使用後啟用 → 可選擇透過 `$B domain-skill promote-to-global` 跨專案推廣。儲存位置和 `/learn` 的每專案學習檔案放在一起。完整參考：**[docs/domain-skills.md](docs/domain-skills.md)**。
- **`$B cdp <Domain.method>`** — 原始 Chrome DevTools Protocol 逃生艙，用於策劃指令無法涵蓋的罕見情況。預設拒絕：方法必須明確加入 `browse/src/cdp-allowlist.ts` 並附上一行理由說明。雙層互斥鎖將瀏覽器範圍的 CDP 呼叫與每個分頁的工作串行化。資料竊取類方法的輸出包裹在 UNTRUSTED 信封中。

> 如果你想要沒有護欄、沒有許可清單、沒有 daemon 的原始 CDP — 只是 agent 到 Chrome 的薄傳輸層？[browser-use/browser-harness-js](https://github.com/browser-use/browser-harness-js) 是不同的哲學（agent 撰寫的 helper vs gstack 的策劃指令），如果你不需要 gstack 的安全堆疊，它是個好選擇。兩者可以共存：gstack 的 `$B cdp` 和 harness 可以透過 Playwright 的 `newCDPSession` 附加到同一個 Chrome。

**[每個 skill 的深度剖析，含範例和理念 →](docs/skills.md)**

### Karpathy 的四個失敗模式？已經涵蓋。

Andrej Karpathy 的 [AI coding 規則](https://github.com/forrestchang/andrej-karpathy-skills)（17K stars）精準點出四個失敗模式：錯誤假設、過度複雜、正交編輯、命令式優先而非宣告式。gstack 的工作流程 skill 全部強制執行這四點。`/office-hours` 在寫程式之前把假設逼出來。Confusion Protocol 阻止 Claude 在架構決策上猜測。`/review` 抓出不必要的複雜性和順便修改的問題。`/ship` 把任務轉化為可驗證的目標，採用測試先行的執行方式。如果你已經在使用 Karpathy 風格的 CLAUDE.md 規則，gstack 就是工作流程執行層，讓這些規則在整個衝刺中都能維持，而不只是單一提示詞。

## 平行衝刺

gstack 用一個衝刺就很強大。十個同時跑的時候才是真正有趣的開始。

**設計是核心。** `/design-consultation` 從零打造你的設計系統、研究現有方案、提出創意風險，並撰寫 `DESIGN.md`。但真正的魔法在於散彈槍到 HTML 的流水線。

**`/design-shotgun` 是你探索的方式。** 描述你想要什麼，它用 GPT Image 生成 4-6 個 AI mockup 變體，然後在瀏覽器裡並排開啟所有變體的對比板。你挑選喜歡的，留下回饋（「更多留白」、「標題更粗」、「去掉漸層」），它生成新一輪。重複直到你喜歡某個結果。幾輪後品味記憶會開始偏向你實際選擇的東西。不用再用文字描述你的願景、然後希望 AI 理解了。你看到選項，挑好的，視覺迭代。

**`/design-html` 讓它成真。** 把核准的 mockup（來自 `/design-shotgun`、CEO 計畫、設計審查，或只是一段描述）變成生產品質的 HTML/CSS。不是那種在某個視窗寬度看起來 OK、其他地方就壞掉的 AI HTML。這個使用 Pretext 進行預計算文字排版：文字在縮放時真的會換行、高度根據內容調整、版型是動態的。30KB 額外負擔，零依賴。偵測你的框架（React、Svelte、Vue）並輸出正確格式。依設計類型智慧路由，選擇不同的 Pretext 模式（登陸頁、儀表板、表單、卡片版型）。輸出是你真的可以上線的東西，不是 demo。

**`/qa` 是個大突破。** 它讓我從 6 個平行工作流程跑到 12 個。Claude Code 說出 *「我看到問題了」*，然後真的修復它、生成迴歸測試、並驗證修復——這改變了我的工作方式。Agent 現在有眼睛了。

**智慧審查路由。** 就像在管理良好的新創公司一樣：CEO 不需要看基礎設施 bug 修復，設計審查在後端變更時不需要執行。gstack 追蹤執行了哪些審查，判斷適合哪些審查，然後就做對的事。審查就緒儀表板在你出貨前告訴你目前狀態。

**全面測試。** 如果你的專案沒有測試框架，`/ship` 從零幫你建立。每次 `/ship` 執行都會產生覆蓋率審計。每個 `/qa` bug 修復都會生成迴歸測試。100% 測試覆蓋率是目標——測試讓感覺驅動的開發變得安全，而不是亂衝的賭博。

**`/document-release` 是你從未有過的工程師。** 它讀取你專案中的每個文件檔案、對照 diff 交叉比對，然後更新所有過時的內容。README、ARCHITECTURE、CONTRIBUTING、CLAUDE.md、TODOS——全部自動保持最新。而且 `/ship` 現在會自動呼叫它——文件不需要額外指令就能保持最新。

**真實瀏覽器模式。** `/open-gstack-browser` 啟動 GStack Browser，一個 AI 控制的 Chromium，具備反偵測隱身、自訂品牌和內建側邊欄擴充功能。Google 和 NYTimes 等網站不需要驗證碼就能運作。選單列顯示「GStack Browser」而非「Chrome for Testing」。你的一般 Chrome 不受影響。所有現有的瀏覽指令都能正常使用。`$B disconnect` 返回無頭模式。只要視窗開著，瀏覽器就會保持運作……不會因為閒置超時而在你工作時被關閉。

**側邊欄 agent — 你的 AI 瀏覽器助理。** 在 Chrome 側面板輸入自然語言，子 Claude 實例就執行它。「導航到設定頁面並截圖。」「用測試資料填寫這個表單。」「瀏覽這個列表中的每個項目並提取價格。」側邊欄自動路由到正確的模型：Sonnet 負責快速操作（點擊、導航、截圖），Opus 負責閱讀和分析。每個任務最多 5 分鐘。側邊欄 agent 在隔離的 session 中運作，不會干擾你的主要 Claude Code 視窗。側邊欄頁腳有一鍵 cookie 匯入。

**個人自動化。** 側邊欄 agent 不只是 dev 工作流程。範例：「瀏覽我孩子學校的家長入口網站，把所有其他家長的姓名、電話和照片加到我的 Google 聯絡人。」有兩種方式取得認證：(1) 在有界面的瀏覽器中登入一次，你的 session 會持久保存；(2) 點擊側邊欄頁腳的「cookies」按鈕，從你的真實 Chrome 匯入 cookies。認證後，Claude 導航目錄、提取資料、建立聯絡人。

**提示注入防禦。** 惡意網頁嘗試劫持你的側邊欄 agent。gstack 提供多層防禦：一個 22MB 的 ML 分類器與瀏覽器一起打包，在本地掃描每個頁面和工具輸出；Claude Haiku 文字稿檢查對整個對話形狀投票；系統提示中的隨機金絲雀 token 跨文字、工具參數、URL 和檔案寫入偵測 session 竊取嘗試；一個裁決組合器要求兩個分類器同意才封鎖（防止單一模型在 Stack Overflow 類頁面上的誤報）。側邊欄標頭的盾牌圖示顯示狀態（綠/黃/紅）。透過 `GSTACK_SECURITY_ENSEMBLE=deberta` 選擇性啟用 721MB 的 DeBERTa-v3 集成，實現 3 取 2 協議。緊急關閉開關：`GSTACK_SECURITY_OFF=1`。完整堆疊參見 [ARCHITECTURE.md](ARCHITECTURE.md#prompt-injection-defense-sidebar-agent)。

**AI 卡住時的瀏覽器交接。** 遇到 CAPTCHA、驗證牆或 MFA 提示？`$B handoff` 在完全相同的頁面開啟可視的 Chrome，並帶上所有你的 cookies 和分頁。解決問題，告訴 Claude 你完成了，`$B resume` 從停下的地方繼續。在連續 3 次失敗後，agent 甚至會自動建議這個操作。

**`/pair-agent` 是跨 agent 協調。** 你在 Claude Code 裡，同時跑著 OpenClaw，或 Hermes，或 Codex。你想讓它們都看著同一個網站。輸入 `/pair-agent`，選你的 agent，然後一個 GStack Browser 視窗開啟讓你觀看。skill 印出一段指令。把那段指令貼到另一個 agent 的聊天裡。它用一次性設定金鑰換取 session token，建立自己的分頁，然後開始瀏覽。你看到兩個 agent 在同一個瀏覽器裡工作，各自在自己的分頁，互不干擾。如果安裝了 ngrok，tunnel 會自動啟動，讓另一個 agent 可以在完全不同的機器上。同機器的 agent 有零摩擦的捷徑，可以直接寫入認證資訊。這是不同供應商的 AI agent 第一次能透過共享瀏覽器協調，並有真實的安全保障：範圍限制的 token、分頁隔離、速率限制、網域限制和活動歸因。

**多 AI 第二意見。** `/codex` 從 OpenAI 的 Codex CLI 取得獨立審查——一個完全不同的 AI 看著同一個 diff。三種模式：帶通過/失敗門檻的程式碼審查、主動嘗試破壞你程式碼的對抗性挑戰，以及帶 session 連續性的開放諮詢。當 `/review`（Claude）和 `/codex`（OpenAI）都審查了同一分支後，你會得到跨模型分析，顯示哪些發現重疊、哪些是各自獨有的。

**隨需安全護欄。** 說「be careful」，`/careful` 就會在任何破壞性指令前警告——rm -rf、DROP TABLE、force-push、git reset --hard。`/freeze` 在除錯時把編輯鎖定到一個目錄，讓 Claude 無法意外「修復」無關的程式碼。`/guard` 同時啟動兩者。`/investigate` 自動凍結到被調查的模組。

**主動 skill 建議。** gstack 注意你處於哪個階段——腦力激盪、審查、除錯、測試——並建議合適的 skill。不喜歡？說「stop suggesting」，它會跨 session 記住。

## 10-15 個平行衝刺

gstack 用一個衝刺就很強大。十個同時跑的時候才真正有了變革性的影響。

[Conductor](https://conductor.build) 讓多個 Claude Code session 平行跑，每個都在自己隔離的工作空間。一個 session 對新想法執行 `/office-hours`，另一個對 PR 做 `/review`，第三個在實作功能，第四個在 staging 上執行 `/qa`，還有六個在其他分支上。全部同時進行。我定期跑 10-15 個平行衝刺——這是目前的實際上限。

衝刺結構才是讓平行工作奏效的關鍵。沒有流程，十個 agent 就是十個混亂的來源。有了流程——思考、規劃、建造、審查、測試、出貨——每個 agent 清楚地知道自己要做什麼、什麼時候停止。你管理它們的方式，就像 CEO 管理一個團隊：關注真正重要的決策，讓其餘的自己跑。

### 語音輸入（AquaVoice、Whisper 等）

gstack skill 有對語音友善的觸發詞組。自然地說出你想要的——「做個安全檢查」、「測試網站」、「做工程審查」——然後正確的 skill 就會啟動。你不需要記住 slash 指令名稱或縮寫。

## 解除安裝

### 選項一：執行解除安裝腳本

如果 gstack 已安裝在你的機器上：

```bash
~/.claude/skills/gstack/bin/gstack-uninstall
```

這會處理 skill、symlink、全域狀態（`~/.gstack/`）、專案本地狀態、browse daemon 和暫存檔。使用 `--keep-state` 保留設定和分析資料。使用 `--force` 跳過確認。

### 選項二：手動移除（沒有本地 repo）

如果你沒有 clone 的 repo（例如你透過 Claude Code 貼上安裝，之後刪除了 clone）：

```bash
# 1. 停止 browse daemon
pkill -f "gstack.*browse" 2>/dev/null || true

# 2. 移除指向 gstack/ 的每個 skill symlink
find ~/.claude/skills -maxdepth 1 -type l 2>/dev/null | while read -r link; do
  case "$(readlink "$link" 2>/dev/null)" in gstack/*|*/gstack/*) rm -f "$link" ;; esac
done

# 3. 移除 gstack
rm -rf ~/.claude/skills/gstack

# 4. 移除全域狀態
rm -rf ~/.gstack

# 5. 移除整合（跳過你從未安裝的）
rm -rf ~/.codex/skills/gstack* 2>/dev/null
rm -rf ~/.factory/skills/gstack* 2>/dev/null
rm -rf ~/.kiro/skills/gstack* 2>/dev/null
rm -rf ~/.openclaw/skills/gstack* 2>/dev/null

# 6. 移除暫存檔
rm -f /tmp/gstack-* 2>/dev/null

# 7. 每個專案清理（在每個專案根目錄執行）
rm -rf .gstack .gstack-worktrees .claude/skills/gstack 2>/dev/null
rm -rf .agents/skills/gstack* .factory/skills/gstack* 2>/dev/null
```

### 清理 CLAUDE.md

解除安裝腳本不會編輯 CLAUDE.md。在每個加入了 gstack 的專案中，移除 `## gstack` 和 `## Skill routing` 區塊。

### Playwright

`~/Library/Caches/ms-playwright/`（macOS）會保留在原處，因為其他工具可能共用它。如果沒有其他工具需要，可以移除。

---

免費，MIT 授權，開源。沒有付費方案，沒有等待名單。

我把我建造軟體的方式開源了。你可以 fork 它，讓它成為你的。

> **我們在招募。** 想要以 AI coding 速度出貨真實產品，並協助強化 gstack 嗎？
> 來 YC 工作 — [ycombinator.com/software](https://ycombinator.com/software)
> 極具競爭力的薪資和股權。舊金山，Dogpatch 區。

## GBrain — 給 coding agent 的持久知識庫

[GBrain](https://github.com/garrytan/gbrain) 是給 AI agent 的持久知識庫——想像它是你的 agent 在 session 之間真正會保留的記憶。GStack 提供了一條從零到「已運行，agent 可以呼叫它」的一指令路徑。

```bash
/setup-gbrain
```

三條路，選一條：

- **Supabase，現有 URL** — 你的雲端 agent 已經建立了一個 brain；貼上 Session Pooler URL，現在這台筆電使用相同的資料。
- **Supabase，自動建立** — 貼上 Supabase Personal Access Token；skill 建立新專案、輪詢直到健康、取得 pooler URL、交給 `gbrain init`。端到端約 90 秒。
- **PGLite 本地** — 不需要帳號、不需要網路，約 30 秒。只在這台 Mac 上的隔離 brain。適合先試試看；之後用 `/setup-gbrain --switch` 遷移到 Supabase。

初始化後，skill 會提議把 gbrain 註冊為 Claude Code 的 MCP 伺服器（`claude mcp add gbrain -- gbrain serve`），讓 `gbrain search`、`gbrain put_page` 等顯示為一等公民的型別化工具——而不是 bash shell 呼叫。

**保持 brain 最新。** 在任何 repo 執行 `/sync-gbrain`，將其程式碼重新索引到 gbrain（預設增量更新，`--full` 完整重新索引，`--dry-run` 預覽）。skill 透過 `gbrain sources add` 將當前目錄註冊為聯合來源，執行 `gbrain sync --strategy code`，並在專案的 CLAUDE.md 中寫入 `## GBrain Search Guidance` 區塊，讓 agent 優先使用 `gbrain search`/`code-def`/`code-refs` 而非 Grep。如果能力檢查失敗，這個區塊會自動移除——不會有指向未安裝工具的過時指引。

**每個遠端的信任策略。** 你機器上的每個 repo 有三個層級之一：

- `read-write` — agent 可以搜尋 brain 並從這個 repo 寫回新頁面
- `read-only` — agent 可以搜尋但不能寫入（最適合多客戶顧問：搜尋共享 brain，但在客戶 B 的 repo 裡工作時不會污染客戶 A 的資料）
- `deny` — 完全不與 gbrain 互動

skill 在每個 repo 只問一次。決定在同一個遠端的所有工作樹和分支間都是持久的。

**GStack 記憶同步（不同功能，相同的私有 repo 基礎設施）。** 選擇性地把你的 gstack 狀態（學習、CEO 計畫、設計文件、回顧、開發者檔案）推送到私有 git repo，讓你的記憶能跨機器跟著你走，有一次性隱私提示（完整許可清單 / 僅限成品 / 關閉）和深度防禦的秘密掃描器，在離開你的機器之前封鎖 AWS 金鑰、token、PEM 區塊和 JWT。

```bash
gstack-brain-init
```

**完整版——每個情境、每個旗標、每個 bin helper、每個疑難排解步驟：** [USING_GBRAIN_WITH_GSTACK.md](USING_GBRAIN_WITH_GSTACK.md)

其他參考資料：[docs/gbrain-sync.md](docs/gbrain-sync.md)（同步專用指南）• [docs/gbrain-sync-errors.md](docs/gbrain-sync-errors.md)（錯誤索引）

## 文件

| 文件 | 涵蓋內容 |
|------|---------|
| [Skill 深度剖析](docs/skills.md) | 每個 skill 的理念、範例和工作流程（含 Greptile 整合）|
| [建造者精神](ETHOS.md) | 建造者哲學：煮沸大湖、先搜尋再建造、三層知識 |
| [搭配 GStack 使用 GBrain](USING_GBRAIN_WITH_GSTACK.md) | `/setup-gbrain` 的每條路徑、旗標、bin helper 和疑難排解步驟 |
| [GBrain 同步](docs/gbrain-sync.md) | 跨機器記憶設定、隱私模式、疑難排解 |
| [架構](ARCHITECTURE.md) | 設計決策和系統內部原理 |
| [瀏覽器參考](BROWSER.md) | `/browse` 的完整指令參考 |
| [貢獻指南](CONTRIBUTING.md) | 開發設定、測試、貢獻者模式和開發模式 |
| [更新日誌](CHANGELOG.md) | 每個版本的新功能 |

## 隱私與遙測

gstack 包含**選擇性加入**的使用遙測，用於協助改善專案。以下是確切的運作方式：

- **預設關閉。** 除非你明確說是，否則不會傳送任何東西到任何地方。
- **第一次執行時，** gstack 詢問你是否想分享匿名使用資料。你可以說不。
- **傳送的內容（如果你選擇加入）：** skill 名稱、持續時間、成功/失敗、gstack 版本、作業系統。就這些。
- **絕對不傳送的內容：** 程式碼、檔案路徑、repo 名稱、分支名稱、提示詞，或任何使用者生成的內容。
- **隨時更改：** `gstack-config set telemetry off` 立即停用一切。

資料儲存在 [Supabase](https://supabase.com)（開源的 Firebase 替代方案）。Schema 在 [`supabase/migrations/`](supabase/migrations/) 中——你可以確認收集了什麼。repo 中的 Supabase 可公開金鑰是公開金鑰（就像 Firebase API key）——行層級安全策略拒絕所有直接存取。遙測透過驗證過的 edge function 流動，強制執行 schema 檢查、事件類型許可清單和欄位長度限制。

**本地分析始終可用。** 執行 `gstack-analytics` 從本地 JSONL 檔案查看你的個人使用儀表板——不需要遠端資料。

## 疑難排解

**Skill 沒有出現？** `cd ~/.claude/skills/gstack && ./setup`

**`/browse` 失敗？** `cd ~/.claude/skills/gstack && bun install && bun run build`

**安裝過期？** 執行 `/gstack-upgrade` — 或在 `~/.gstack/config.yaml` 設定 `auto_upgrade: true`

**想要更短的指令？** `cd ~/.claude/skills/gstack && ./setup --no-prefix` — 從 `/gstack-qa` 切換到 `/qa`。你的選擇在未來升級時會被記住。

**想要有命名空間的指令？** `cd ~/.claude/skills/gstack && ./setup --prefix` — 從 `/qa` 切換到 `/gstack-qa`。如果你同時執行其他 skill 套件，這很有用。

**Codex 說「Skipped loading skill(s) due to invalid SKILL.md」？** 你的 Codex skill 描述已過時。修復方法：`cd ~/.codex/skills/gstack && git pull && ./setup --host codex` — 或對於 repo 本地安裝：`cd "$(readlink -f .agents/skills/gstack)" && git pull && ./setup --host codex`

**Windows 使用者：** gstack 在 Windows 11 上透過 Git Bash 或 WSL 運作。除了 Bun 之外還需要 Node.js——Bun 在 Windows 上的 Playwright pipe transport 有已知 bug（[bun#4253](https://github.com/oven-sh/bun/issues/4253)）。browse 伺服器會自動退回使用 Node.js。確保 `bun` 和 `node` 都在你的 PATH 中。

**Claude 說看不到 skill？** 確認你的專案 `CLAUDE.md` 有 gstack 區塊。加入以下內容：

```
## gstack
Use /browse from gstack for all web browsing. Never use mcp__claude-in-chrome__* tools.
Available skills: /office-hours, /plan-ceo-review, /plan-eng-review, /plan-design-review,
/design-consultation, /design-shotgun, /design-html, /review, /ship, /land-and-deploy,
/canary, /benchmark, /browse, /open-gstack-browser, /qa, /qa-only, /design-review,
/setup-browser-cookies, /setup-deploy, /setup-gbrain, /sync-gbrain, /retro, /investigate, /document-release,
/codex, /cso, /autoplan, /pair-agent, /careful, /freeze, /guard, /unfreeze, /gstack-upgrade, /learn.
```

## 授權

MIT。永久免費。去做些什麼吧。
