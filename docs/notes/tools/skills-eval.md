# Skills 評比表

## 評分標準

| 項目 | 1 ⭐ | 3 ⭐ | 5 ⭐ |
|------|------|------|------|
| **效果** | 產出需大幅人工修正 | 產出可用，小幅調整 | 產出直接可用 |
| **省時** | 比自己做還慢 | 省 30-50% 時間 | 省 70%+ 時間 |

狀態：`候選` / `進行中` / `已驗證`

---

## 來源說明

| 來源 | GitHub | 說明 |
|------|--------|------|
| **everything-claude-code** | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | 透過 Plugin 安裝至 `~/.claude/skills/` |
| **Claude Code 原生** | — | 路徑前綴 `builtin:`，不在 `~/.claude/skills/` 目錄下（如 `security-review`） |
| **superpowers** | [claude-plugins-official](https://github.com/anthropics/claude-plugins) | Anthropic 官方插件 v5.0.7 |
| **gstack** | [garrytan/gstack](https://github.com/garrytan/gstack) | Garry Tan（YC CEO）23 個角色化工具，88.7K stars |
| **agency-agents** | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | 144+ 角色化工具，**全部為 agents**，透過 Agent tool 呼叫，不在本表列出 → 見 [agents-eval.md](agents-eval.md) |
| **專案本地** | — | 本專案自訂（`.claude/skills/` / `.cursor/skills/`） |

---

## 實驗假設

開始驗證前的預期，完成後對照實際結果：

| 假設 | 預期 | 實際結果 |
|------|------|---------|
| gstack `review` 比內建 `python-review` 找到更多問題 | gstack 有角色設定更深入 | 待驗證 |
| gstack `cso` 比內建 `security-review` 覆蓋更廣 | gstack 有 OWASP+STRIDE 雙框架 | 待驗證 |
| `refactor-clean` 一次跑完整檔案比手動快 | 省 50%+ 時間 | 待驗證 |
| `tdd-workflow` 強制先寫測試比直接寫 code 品質更高 | 覆蓋率更高、bug 更少 | 待驗證 |

---

## 候選清單（依產品化維度）

### 程式品質

| Skill | 來源 | 用途 | 優先度 | 狀態 |
|-------|------|------|--------|------|
| `python-patterns` | everything-claude-code | Python 最佳實踐、型別標注 | 🔴 高 | 候選 |
| `python-review` | everything-claude-code | 深度 code review | 🔴 高 | 候選 |
| `review` | gstack | Staff Engineer 角色，抓 production bug，可自動修 | 🔴 高 | 候選 |
| `code-best-practice` | 專案本地 | PyMC-Marketing 程式風格與慣例 | 🔴 高 | 候選 |

### 重構

| Skill | 來源 | 用途 | 優先度 | 狀態 |
|-------|------|------|--------|------|
| `refactor-clean` | everything-claude-code | 清除死碼、統一結構 | 🔴 高 | 候選 |

### 測試

| Skill | 來源 | 用途 | 優先度 | 狀態 |
|-------|------|------|--------|------|
| `python-testing` | everything-claude-code | pytest 策略、coverage 達標 | 🔴 高 | 候選 |
| `tdd-workflow` | everything-claude-code | 測試先行流程 | 🔴 高 | 候選 |
| `superpowers:test-driven-development` | superpowers | TDD 完整工作流 | 🔴 高 | 候選 |
| `e2e-testing` | everything-claude-code | 關鍵用戶流程驗證 | 🟡 中 | 候選 |
| `qa` | gstack | QA Lead 角色，瀏覽器測試 + bug 修復 + 回歸測試 | 🟡 中 | 候選 |

### 安全

| Skill | 來源 | 用途 | 優先度 | 狀態 |
|-------|------|------|--------|------|
| `security-review` | Claude Code 原生 | 掃描 API key 洩漏、注入風險 | 🔴 高 | 候選 |
| `cso` | gstack | Chief Security Officer，OWASP Top 10 + STRIDE | 🟡 中 | 候選 |

### UI/UX

| Skill | 來源 | 用途 | 優先度 | 狀態 |
|-------|------|------|--------|------|
| `design-review` | gstack | Designer-Coder 角色，UI 審查 + 截圖 + 即時修改 | 🟡 中 | 候選 |
| `design-consultation` | gstack | 完整設計系統研究 + mockup | 🟢 低 | 候選 |

### 規劃與策略

| Skill | 來源 | 用途 | 優先度 | 狀態 |
|-------|------|------|--------|------|
| `superpowers:write-plan` | superpowers | 結構化實作計畫 | 🔴 高 | 候選 |
| `superpowers:executing-plans` | superpowers | 執行計畫工作流 | 🔴 高 | 候選 |
| `autoplan` | gstack | CEO→Design→Eng 三角審查流水線 | 🟡 中 | 候選 |
| `plan-eng-review` | gstack | Eng Manager 角色，架構 + 資料流 + 測試矩陣 | 🟡 中 | 候選 |
| `office-hours` | gstack | YC Office Hours 模式，產品逼問 | 🟢 低 | 候選 |

### 部署與發布

| Skill | 來源 | 用途 | 優先度 | 狀態 |
|-------|------|------|--------|------|
| `setup-deploy` | gstack | 一次性部署設定 | 🟡 中 | 候選 |
| `ship` | gstack | Release Engineer：sync + test + PR push | 🟡 中 | 候選 |
| `land-and-deploy` | gstack | PR merge + CI wait + production 驗證 | 🟡 中 | 候選 |
| `canary` | gstack | SRE：部署後監控錯誤、回歸 | 🟢 低 | 候選 |

### 效能與文件

| Skill | 來源 | 用途 | 優先度 | 狀態 |
|-------|------|------|--------|------|
| `benchmark` | gstack | 頁面載入、Core Web Vitals 基準 | 🟢 低 | 候選 |
| `update-docs` | everything-claude-code | 自動更新 README、文件 | 🟡 中 | 候選 |
| `document-release` | gstack | Technical Writer，ship 後自動更新所有文件 | 🟡 中 | 候選 |

### MMM 領域

| Skill | 來源 | 用途 | 優先度 | 狀態 |
|-------|------|------|--------|------|
| `mmm-modeling` | 專案本地 | MMM 模型建構、擬合、診斷 | 🔴 高 | 候選 |

---

## 評比紀錄

### refactor-clean
- **來源**：everything-claude-code
- **任務**：整理 `ai_analysis.py`，移除死碼、抽取重複邏輯
- **呼叫方式**：Skill tool
- **效果**：產出結構化的死碼分類表（SAFE/CAUTION/DANGER），指引刪除 `channel_cols` 死碼與抽出 `_make_client`、`_compute_fit_metrics` 兩個 helper；函數從最長 68 行縮短至 < 50 行
- **優點**：提供清晰的安全分級流程，避免盲目刪除；Step 5 的「整合重複」指引對抽 helper 很有效
- **限制**：以死碼偵測為主軸，無法直接要求「加 error handling」或「改型別標注」；vulture 對跨檔呼叫誤報 60% 信心，需人工確認
- **評分**：效果 ⭐⭐⭐⭐ / 省時 ⭐⭐⭐⭐
- **適合場景**：清理已有一段時間的模組、移除廢棄參數、整合重複的初始化邏輯
- **驗證日期**：2026-05-04

### python-review
- **來源**：everything-claude-code
- **任務**：審查 `refactor-clean` 完成後的 `ai_analysis.py`
- **呼叫方式**：Skill tool → python-reviewer agent
- **效果**：發現 2 HIGH（`_make_client` 缺回傳型別、`mmm` 參數無型別）、4 MEDIUM（行長、chr(10) workaround、client 未快取、缺 error handling）；均有具體修法
- **優點**：分級明確（CRITICAL/HIGH/MEDIUM），每條有 before/after 範例；mypy 整合讓型別問題無法漏網
- **限制**：不自動修正，只報告；MEDIUM 中的「client 未快取」在 Streamlit 場景不是實際問題（每次渲染一次），略有過度警示
- **評分**：效果 ⭐⭐⭐⭐⭐ / 省時 ⭐⭐⭐⭐
- **適合場景**：任何 Python 改動後的驗收，特別是有 type hint 要求的場景
- **驗證日期**：2026-05-04

### tdd-workflow
- **來源**：everything-claude-code
- **任務**：為 `streamlit/mmm-demo/components/mmm_runner.py` 的純函數建立單元測試
- **呼叫方式**：Skill tool
- **效果**：產出 31 個單元測試（5 class，涵蓋 `prepare_features`、`saved_model_exists`、`ensure_model_file`、`load_sample_data`、`get_channel_roas`、`save_mmm`、`load_mmm`）；整體覆蓋率 71%，testable 函數覆蓋率 100%；HF Hub 下載路徑用 mock 覆蓋
- **優點**：流程明確（RED→GREEN→REFACTOR）；mock 指引對 xarray idata 複雜 chain 有效；edge case 提示（zero spend、zero channel、missing dataset）很到位
- **限制**：MCMC 函數（`build_mmm`、`fit_mmm`、`sample_posterior_predictive`）無法在不啟動 PyMC 的情況下測試，整體覆蓋率受限於此；skill 文件偏 TS/JS 框架，pytest 範例較少需自行對應
- **評分**：效果 ⭐⭐⭐⭐ / 省時 ⭐⭐⭐⭐
- **適合場景**：為純函數、資料處理管線、mock 友好的 API wrapper 建立測試；適合快速提升新模組的 test coverage
- **驗證日期**：2026-05-04

### security-review
- **來源**：Claude Code 原生
- **任務**：掃描 `streamlit/mmm-demo/` 的 API key 處理、hardcode 風險、LLM output 渲染
- **呼叫方式**：Skill tool → 內建 security-reviewer agent
- **效果**：自動分析 git diff，輸出結構化報告（CRITICAL/HIGH/MEDIUM），本次無高信心弱點
- **優點**：速度快，聚焦 PR diff，signal-to-noise 極高；自動排除 false positive 類型
- **限制**：覆蓋範圍限於 PR diff，不做全專案掃描；無 OWASP/STRIDE 框架輸出
- **評分**：效果 ⭐⭐⭐⭐ / 省時 ⭐⭐⭐⭐⭐
- **適合場景**：每次 PR 前快速驗收，日常 commit 安全把關
- **驗證日期**：2026-05-04

### cso
- **來源**：gstack
- **任務**：對 `streamlit/mmm-demo/` 全相位安全掃描（Phase 0–14，OWASP+STRIDE）
- **呼叫方式**：Skill tool
- **效果**：Attack surface census、git history 掃描、LLM security、OWASP Top 10、STRIDE，本次無高信心弱點；與 `security-review` 結論一致
- **優點**：覆蓋最廣（14 phases），STRIDE 威脅模型對架構設計階段有參考價值；`--diff` 模式可對齊 PR workflow
- **限制**：preamble script 須 bash 環境，在 Windows PowerShell 需手動跳過部分步驟；對純本地 Streamlit 專案 CI/CD phase 輸出空白，略顯冗餘
- **評分**：效果 ⭐⭐⭐⭐ / 省時 ⭐⭐⭐（較慢）
- **適合場景**：月度深度掃描、架構設計審查、部署前驗收
- **驗證日期**：2026-05-04

### design-review（gstack）
- **來源**：gstack
- **任務**：對 `streamlit/mmm-demo/` 5 頁 UI 進行視覺稽核，截圖後逐頁分析 UX 問題
- **呼叫方式**：Skill tool
- **效果**：發現 2 HIGH 問題：(1) 鎖定頁面警告無導航連結（使用者卡住）；(2) CSS nth-child 鎖頁邏輯位置依賴，任何頁面順序改動都會靜默鎖錯；兩項均有具體修法並已實施
- **優點**：截圖驅動，能發現純靜態分析看不到的 UX 問題；問題分級（BLOCKER/HIGH/LOW）清晰，不會把所有問題等量齊觀；對 Streamlit 的 CSS 注入機制理解正確
- **限制**：需要 `$B` browse binary，且截圖路徑有白名單限制（須在 `Temp` 或專案目錄下）；Windows PowerShell 環境的 preamble 部分須 bash，需跳過；Streamlit session_state 在無模型時截圖只能看到初始狀態（locked pages 無法截到有內容的畫面）
- **評分**：效果 ⭐⭐⭐⭐⭐ / 省時 ⭐⭐⭐⭐
- **適合場景**：UI 改動後的視覺驗收；新頁面上線前的 UX 問題排查；Streamlit 多頁應用的導航流程審查
- **驗證日期**：2026-05-04

### setup-deploy（gstack）
- **來源**：gstack
- **任務**：為 mmm-demo Streamlit Cloud 部署設定生命週期，寫入 CLAUDE.md 讓 `/land-and-deploy` 可讀取
- **呼叫方式**：Skill tool
- **效果**：引導確認平台（Streamlit Cloud）、production URL、部署方式（push to main 自動觸發）；health check 驗證 HTTP 303（正常）；寫入 CLAUDE.md `## Deploy Configuration` 標準格式
- **優點**：設定存在 CLAUDE.md，所有後續 gstack skill 都能讀取；偵測流程覆蓋主流平台（fly/render/vercel/netlify/heroku/railway）；idempotent，重跑只會覆寫不會衝突
- **限制**：本專案已有既有部署，skill 主要做設定文件化而非真正建立部署；Streamlit Cloud 無 CLI 可執行 status 查詢，只能靠 HTTP poll；升級到 gstack v1.26 時觸發 writing style migration，會多問一次偏好設定
- **評分**：效果 ⭐⭐⭐⭐ / 省時 ⭐⭐⭐⭐
- **適合場景**：新專案第一次設定部署；換平台後重新文件化；為 `/land-and-deploy` 做前置設定
- **驗證日期**：2026-05-06

### design-shotgun（gstack）
- **來源**：gstack
- **任務**：將 mmm-demo 5 頁 Streamlit UI 從 emoji 風格重做為 Material Icons + C-style 企業 UI（深色側邊欄、淺灰主區、藍色強調色）
- **呼叫方式**：Skill tool
- **效果**：
  - 建立 `components/ui_helpers.py`（`icon_title`、`icon_header`、`icon_subheader` 三個 HTML helper），用 Material Symbols Rounded 字型渲染圖示
  - 修改 `app.py`、所有 5 個頁面檔案：emoji → Material Icons，`st.button` / `st.page_link` 改用 `:material/xxx:` 語法
  - 解決 `<h1>/<h3>` flex 垂直置中問題（改用 `<div>` container + `display:block` icon span）
  - 翻譯 `docs/install/gstack.zh-tw.md`（完整繁體中文版）
- **優點**：
  - 設計決策明確（字型大小對齊 Streamlit theme：title=2.25rem、header=1.75rem、subheader=1.5rem）
  - 先確認技術可行性（驗證 Streamlit 本地 woff2、`font-family:'Material Symbols Rounded'`、ligature 渲染機制）再動手
  - 遇到 `st.title(icon=)` 不支援的技術限制，提出 `unsafe_allow_html` HTML helper 替代方案
- **限制**：
  - `st.title()`、`st.header()`、`st.subheader()` 原生不支援 `icon=` 參數，必須繞道 HTML 注入
  - 垂直置中問題需多次試錯（inline-flex → display:block → `<div>` container）
  - Windows PowerShell 環境 preamble 部分須跳過（bash 限定）；C-style 全域 CSS 需透過 `components/progress.py` 注入，跨頁面樣式需統一管控
- **評分**：效果 ⭐⭐⭐⭐ / 省時 ⭐⭐⭐⭐
- **適合場景**：UI 整體風格升級；從 prototype emoji 風格升至企業匯報品質；需要設計系統一致性的多頁 Streamlit 應用
- **驗證日期**：2026-05-06

### qa（gstack）
- **來源**：gstack
- **任務**：對 mmm-demo 5 頁 Streamlit UI 進行真瀏覽器 QA，驗收 04b 設計重做後的 Material Icons 顯示、版型與導航正確性
- **呼叫方式**：Skill tool → `$B` browse binary（Chromium headless）
- **效果**：全 5 頁截圖完整；Material Icons（analytics、table_chart、model_training、stacked_bar_chart、savings）全部正確渲染；鎖定頁「前往模型擬合」導航連結確認存在；無 uncaught JS exception；健康分數 95/100
- **優點**：真瀏覽器渲染，能確認字型 ligature（Material Symbols Rounded）實際顯示；截圖可直接作為驗收佐證；`$B js` 可查 performance entries 精確定位 404 資源來源
- **限制**：Streamlit SPA 直接 `goto` 子頁面後需等待 3 秒才能截到有內容的畫面（頁面初始化時間）；`snapshot -i -a` 在 Streamlit 多元素頁面觸發「matched multiple elements」錯誤，需改用 `screenshot`；MCMC 後的完整頁面（頻道貢獻、預算最佳化有資料狀態）無法在無模型下測試
- **評分**：效果 ⭐⭐⭐⭐⭐ / 省時 ⭐⭐⭐⭐
- **適合場景**：UI 改動後的視覺驗收；多頁 Streamlit app 的跨頁導航與 icon 渲染確認；設計迭代後的快速回歸截圖
- **驗證日期**：2026-05-07

### benchmark（gstack）
- **來源**：gstack
- **任務**：對 mmm-demo 5 頁 Streamlit app 進行效能基準測試，建立 baseline 供後續版本比較
- **呼叫方式**：Skill tool → `$B goto` + `$B perf`（Chromium headless）
- **效果**：完整收集 5 頁 load time 指標；所有頁面 total load < 70ms（本機 localhost）；無任何頁面逾 200ms；baseline 儲存至 `.gstack/benchmark-reports/baselines/baseline.json`；截圖存檔佐證
- **數據**：首頁 41ms、資料總覽 58ms、模型擬合 69ms（最慢，含 MCMC state check）、頻道貢獻 42ms、預算最佳化 43ms；平均 51ms
- **優點**：`$B perf` 一行命令輸出 dns/tcp/ssl/ttfb/domParse/domReady/load 全維度指標；自動識別 localhost 環境（dns/tcp 均 0，ttfb 為純 Streamlit server 延遲）；結構化 JSON baseline 可供 CI 比較回歸
- **限制**：`$B eval` 多行 JS（`JSON.stringify(...)`) 在 Windows 環境 exit code 1，無法取得 ResourceTiming entries；`$B errors` 命令不存在，console error 無法直接捕捉；本機 localhost 數據不代表生產環境（無網路延遲）
- **評分**：效果 ⭐⭐⭐⭐ / 省時 ⭐⭐⭐⭐⭐
- **適合場景**：UI 重構前後的效能回歸對比；建立效能基準讓 CI 可守門；找出特定頁面的慢載入根因（透過 ResourceTiming entries）
- **驗證日期**：2026-05-07

### canary（gstack）
- **來源**：gstack
- **任務**：對 mmm-demo（localhost:8501）執行 `--quick` 單次健康檢查，比對 Task 08 建立的 baseline
- **呼叫方式**：Skill tool → `$B goto` + `$B perf` + `$B screenshot`（Chromium headless）
- **效果**：全 5 頁 HTTP 200；warm 頁面（2-5）全部比 baseline 快 34-61%；截圖 3 張佐證；無任何 CRITICAL/HIGH alert
- **數據對比**：

| 頁面 | baseline | canary | 變化 |
|------|---------|--------|------|
| 首頁 | 41ms | 751ms | cold-start TCP，正常 |
| 資料總覽 | 58ms | 38ms | -34% |
| 模型擬合 | 69ms | 27ms | -61% |
| 頻道貢獻 | 42ms | 25ms | -40% |
| 預算最佳化 | 43ms | 26ms | -40% |

- **Cloud 數據**（https://pymc-marketing-mmm.streamlit.app/）：首頁 5499ms（container cold-start）、warm 頁 450–536ms（TTFB ≈ 350ms 為跨洋 RTT）、全 5 頁 HEALTHY
- **優點**：與 benchmark baseline 直接對比，馬上看出冷啟動 vs 暖連線差異；`$B perf` 快速取得結構化數據；截圖作為健康佐證；alert 機制設計合理（2x baseline 才觸發）；同一 skill 可同時跑 localhost 和 cloud URL
- **限制**：`--quick` 模式只跑一次，無法偵測偶發問題；`$B console --errors` 命令不存在，無法直接捕捉 JS console 錯誤；localhost baseline 與 cloud 數據差距 10x，需分別建立兩份 baseline 才有意義
- **評分**：效果 ⭐⭐⭐⭐ / 省時 ⭐⭐⭐⭐⭐
- **適合場景**：每次 push 後的快速健康確認；部署後的雲端首次驗收；localhost 與生產環境效能差異量化
- **驗證日期**：2026-05-07

### document-release（gstack）
- **來源**：gstack
- **任務**：對 mmm-demo 產品化實驗（iterations 4b–8）後的文件做整體同步與修正
- **呼叫方式**：Skill tool
- **效果**：
  - `streamlit/mmm-demo/README.zh-TW.md`：移除重複行、補齊目錄結構（run.ps1、ui_helpers.py、progress.py、tests/）、修正 AI expander 標籤（移除 emoji）
  - `.claude/CLAUDE.md`：修正過時路徑（sandbox/streamlit_demo → streamlit/mmm-demo）
  - `docs/notes/workflow/best-practices.md`：流水線從 6 步擴展至 9 步、安全掃描對比修正為完成
  - `docs/notes/workflow/action-plan.md`：tasks 5/8 標記完成、task 9 進行中
- **優點**：自動偵測過時路徑、重複行、目錄結構缺漏；分類 auto-update（直接修正）vs ask-user（風險變更）；跨文件一致性檢查（action-plan vs README vs best-practices）
- **限制**：on main branch 時 PR 相關步驟（body update、title sync）無法執行；`gh auth` 未設定則無法操作 GitHub PR；需要先了解整個實驗 context 才能判斷哪些是 stale（不能盲目信任 diff）
- **評分**：效果 ⭐⭐⭐⭐ / 省時 ⭐⭐⭐⭐
- **適合場景**：多次迭代後的文件整體同步；發現路徑、標籤、目錄結構等 factual 錯誤；跨文件狀態（任務進度）一致性維護
- **驗證日期**：2026-05-07

### retro（gstack）
- **來源**：gstack
- **任務**：對 mmm-demo 產品化實驗（7 天，2026-04-30 → 2026-05-07）執行工程回顧
- **呼叫方式**：Skill tool → git log + shortstat + session 偵測 + skill usage analytics
- **效果**：17 commits、8 sessions、feat 53%/docs 24%、skill usage 彙整（/benchmark /canary /document-release）、Ship of Week 自動識別（design-shotgun）、3 改善點 + 3 下週習慣
- **優點**：自動從 git log 萃取所有指標，不需人工整理；session 偵測（45 分鐘 gap）準確區分 deep/medium/micro；skill-usage.jsonl 整合讓工具效果可視化；snapshot JSON 供未來趨勢對比
- **限制**：repo import commit（674k LOC）會嚴重扭曲 raw LOC 指標，需手動排除解讀；test ratio 計算以 test 關鍵字判斷，對 Streamlit 頁面類型不精確；`.context/retros/` JSON 人類不可讀，需另建 task 文件補充
- **評分**：效果 ⭐⭐⭐⭐ / 省時 ⭐⭐⭐⭐⭐
- **適合場景**：每輪開發週期結束後的整體回顧；solo 專案追蹤個人工作模式；建立跨週趨勢基準
- **驗證日期**：2026-05-07
