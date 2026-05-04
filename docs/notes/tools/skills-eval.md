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

<!-- 格式：
### skill-name
- **來源**：內建 / superpowers / gstack / 專案本地
- **任務**：做了什麼
- **呼叫方式**：/skill-name 或 Skill tool
- **效果**：實際產出描述
- **優點**：
- **限制**：
- **評分**：效果 ⭐x / 省時 ⭐x
- **適合場景**：
- **驗證日期**：
-->
