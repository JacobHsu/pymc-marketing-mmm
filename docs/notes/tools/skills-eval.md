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
| **內建** | — | Claude Code 全局內建（`~/.claude/.agents/skills/`） |
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
| `python-patterns` | 內建 | Python 最佳實踐、型別標注 | 🔴 高 | 候選 |
| `python-review` | 內建 | 深度 code review | 🔴 高 | 候選 |
| `review` | gstack | Staff Engineer 角色，抓 production bug，可自動修 | 🔴 高 | 候選 |
| `code-best-practice` | 專案本地 | PyMC-Marketing 程式風格與慣例 | 🔴 高 | 候選 |

### 重構

| Skill | 來源 | 用途 | 優先度 | 狀態 |
|-------|------|------|--------|------|
| `refactor-clean` | 內建 | 清除死碼、統一結構 | 🔴 高 | 候選 |

### 測試

| Skill | 來源 | 用途 | 優先度 | 狀態 |
|-------|------|------|--------|------|
| `python-testing` | 內建 | pytest 策略、coverage 達標 | 🔴 高 | 候選 |
| `tdd-workflow` | 內建 | 測試先行流程 | 🔴 高 | 候選 |
| `superpowers:test-driven-development` | superpowers | TDD 完整工作流 | 🔴 高 | 候選 |
| `e2e-testing` | 內建 | 關鍵用戶流程驗證 | 🟡 中 | 候選 |
| `qa` | gstack | QA Lead 角色，瀏覽器測試 + bug 修復 + 回歸測試 | 🟡 中 | 候選 |

### 安全

| Skill | 來源 | 用途 | 優先度 | 狀態 |
|-------|------|------|--------|------|
| `security-review` | 內建 | 掃描 API key 洩漏、注入風險 | 🔴 高 | 候選 |
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
| `update-docs` | 內建 | 自動更新 README、文件 | 🟡 中 | 候選 |
| `document-release` | gstack | Technical Writer，ship 後自動更新所有文件 | 🟡 中 | 候選 |

### MMM 領域

| Skill | 來源 | 用途 | 優先度 | 狀態 |
|-------|------|------|--------|------|
| `mmm-modeling` | 專案本地 | MMM 模型建構、擬合、診斷 | 🔴 高 | 候選 |

---

## 評比紀錄

### refactor-clean
- **來源**：內建
- **任務**：整理 `ai_analysis.py`，移除死碼、抽取重複邏輯
- **呼叫方式**：Skill tool
- **效果**：產出結構化的死碼分類表（SAFE/CAUTION/DANGER），指引刪除 `channel_cols` 死碼與抽出 `_make_client`、`_compute_fit_metrics` 兩個 helper；函數從最長 68 行縮短至 < 50 行
- **優點**：提供清晰的安全分級流程，避免盲目刪除；Step 5 的「整合重複」指引對抽 helper 很有效
- **限制**：以死碼偵測為主軸，無法直接要求「加 error handling」或「改型別標注」；vulture 對跨檔呼叫誤報 60% 信心，需人工確認
- **評分**：效果 ⭐⭐⭐⭐ / 省時 ⭐⭐⭐⭐
- **適合場景**：清理已有一段時間的模組、移除廢棄參數、整合重複的初始化邏輯
- **驗證日期**：2026-05-04

### python-review
- **來源**：內建
- **任務**：審查 `refactor-clean` 完成後的 `ai_analysis.py`
- **呼叫方式**：Skill tool → python-reviewer agent
- **效果**：發現 2 HIGH（`_make_client` 缺回傳型別、`mmm` 參數無型別）、4 MEDIUM（行長、chr(10) workaround、client 未快取、缺 error handling）；均有具體修法
- **優點**：分級明確（CRITICAL/HIGH/MEDIUM），每條有 before/after 範例；mypy 整合讓型別問題無法漏網
- **限制**：不自動修正，只報告；MEDIUM 中的「client 未快取」在 Streamlit 場景不是實際問題（每次渲染一次），略有過度警示
- **評分**：效果 ⭐⭐⭐⭐⭐ / 省時 ⭐⭐⭐⭐
- **適合場景**：任何 Python 改動後的驗收，特別是有 type hint 要求的場景
- **驗證日期**：2026-05-04

### tdd-workflow
- **來源**：userSettings
- **任務**：為 `streamlit/mmm-demo/components/mmm_runner.py` 的純函數建立單元測試
- **呼叫方式**：Skill tool
- **效果**：產出 31 個單元測試（5 class，涵蓋 `prepare_features`、`saved_model_exists`、`ensure_model_file`、`load_sample_data`、`get_channel_roas`、`save_mmm`、`load_mmm`）；整體覆蓋率 71%，testable 函數覆蓋率 100%；HF Hub 下載路徑用 mock 覆蓋
- **優點**：流程明確（RED→GREEN→REFACTOR）；mock 指引對 xarray idata 複雜 chain 有效；edge case 提示（zero spend、zero channel、missing dataset）很到位
- **限制**：MCMC 函數（`build_mmm`、`fit_mmm`、`sample_posterior_predictive`）無法在不啟動 PyMC 的情況下測試，整體覆蓋率受限於此；skill 文件偏 TS/JS 框架，pytest 範例較少需自行對應
- **評分**：效果 ⭐⭐⭐⭐ / 省時 ⭐⭐⭐⭐
- **適合場景**：為純函數、資料處理管線、mock 友好的 API wrapper 建立測試；適合快速提升新模組的 test coverage
- **驗證日期**：2026-05-04

### security-review
- **來源**：內建
- **任務**：掃描 `streamlit/mmm-demo/` 的 API key 處理、hardcode 風險、LLM output 渲染
- **呼叫方式**：Skill tool → 內建 security-reviewer agent
- **效果**：自動分析 git diff，輸出結構化報告（CRITICAL/HIGH/MEDIUM），本次無高信心弱點
- **優點**：速度快，聚焦 PR diff，signal-to-noise 極高；自動排除 false positive 類型
- **限制**：覆蓋範圍限於 PR diff，不做全專案掃描；無 OWASP/STRIDE 框架輸出
- **評分**：效果 ⭐⭐⭐⭐ / 省時 ⭐⭐⭐⭐⭐
- **適合場景**：每次 PR 前快速驗收，日常 commit 安全把關
- **驗證日期**：2026-05-04

### cso（gstack）
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
- **驗證日期**：2026-05-04
