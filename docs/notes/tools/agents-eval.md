# Agents 評比表

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
| **用戶自定義** | — | `~/.claude/agents/`，來源待確認（可能為規則包或手動建立） |
| **agency-agents** | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | 144+ 角色化 agent，12 部門，MIT 授權 |
| **SDK 內建** | — | Claude Agent SDK 提供的 subagent_type |

---

## 實驗假設

開始驗證前的預期，完成後對照實際結果：

| 假設 | 預期 | 實際結果 |
|------|------|---------|
| agency-agents `Code Reviewer` 比本地 `code-reviewer` 更全面 | agency-agents 有專業角色設定 | 待驗證 |
| `Evidence Collector` 能有效防止 Claude 幻想完成 | 強制截圖佐證，拒絕未驗證宣稱 | 待驗證 |
| `Explore`（SDK）比直接讀檔更快定位問題 | 唯讀且跨檔案分析能力強 | 待驗證 |
| 雙 agent 並行（本地 + agency-agents）比單一 agent 更準確 | 兩個觀點交叉驗證 | 待驗證 |

---

## 候選清單（依產品化維度）

### 程式品質與架構

| Agent | 來源 | subagent_type / 呼叫 | 用途 | 優先度 | 狀態 |
|-------|------|---------------------|------|--------|------|
| `code-reviewer` | 用戶自定義 | 本地 agent | 每次改動後即時 review | 🔴 高 | 候選 |
| `Code Reviewer` | agency-agents | `Code Reviewer` | 品質、安全、可維護性審查 | 🔴 高 | 候選 |
| `python-reviewer` | SDK 內建 | `python-reviewer` | Python 型別、安全、效能專項 | 🔴 高 | 候選 |
| `Software Architect` | agency-agents | `Software Architect` | 系統設計、DDD、架構決策 | 🟡 中 | 候選 |
| `refactor-cleaner` | 用戶自定義 | 本地 agent | 清理大檔案死碼 | 🔴 高 | 候選 |

### 規劃

| Agent | 來源 | subagent_type / 呼叫 | 用途 | 優先度 | 狀態 |
|-------|------|---------------------|------|--------|------|
| `planner` | 用戶自定義 | 本地 agent | 產品化路線規劃、拆分迭代 | 🔴 高 | 候選 |
| `architect` | 用戶自定義 | 本地 agent | 模組架構設計 | 🟡 中 | 候選 |
| `Product Manager` | agency-agents | `Product Manager` | 完整產品生命週期管理 | 🟡 中 | 候選 |

### 測試

| Agent | 來源 | subagent_type / 呼叫 | 用途 | 優先度 | 狀態 |
|-------|------|---------------------|------|--------|------|
| `tdd-guide` | 用戶自定義 | 本地 agent | 強制測試先行流程 | 🔴 高 | 候選 |
| `e2e-runner` | 用戶自定義 | 本地 agent | 跑關鍵用戶流程測試 | 🟡 中 | 候選 |
| `Evidence Collector` | agency-agents | `Evidence Collector` | 截圖佐證，拒絕幻想，找 3-5 個問題 | 🟡 中 | 候選 |
| `Reality Checker` | agency-agents | `Reality Checker` | 停止幻想核可，要求壓倒性證據 | 🟡 中 | 候選 |
| `Performance Benchmarker` | agency-agents | `Performance Benchmarker` | 效能測試與分析 | 🟢 低 | 候選 |
| `API Tester` | agency-agents | `API Tester` | API 驗證與效能測試 | 🟡 中 | 候選 |

### 安全

| Agent | 來源 | subagent_type / 呼叫 | 用途 | 優先度 | 狀態 |
|-------|------|---------------------|------|--------|------|
| `security-reviewer` | 用戶自定義 | 本地 agent | commit 前安全掃描 | 🔴 高 | 候選 |
| `Security Engineer` | agency-agents | `Security Engineer` | 威脅建模、安全架構、事件回應 | 🟡 中 | 候選 |

### 探索與除錯

| Agent | 來源 | subagent_type / 呼叫 | 用途 | 優先度 | 狀態 |
|-------|------|---------------------|------|--------|------|
| `Explore` | SDK 內建 | `Explore` | 程式庫探索、唯讀分析 | 🔴 高 | 候選 |
| `Codebase Onboarding Engineer` | agency-agents | `Codebase Onboarding Engineer` | 快速理解陌生程式庫 | 🟡 中 | 候選 |

### 文件

| Agent | 來源 | subagent_type / 呼叫 | 用途 | 優先度 | 狀態 |
|-------|------|---------------------|------|--------|------|
| `doc-updater` | 用戶自定義 | 本地 agent | 同步更新 README.zh-TW.md | 🟡 中 | 候選 |
| `Technical Writer` | agency-agents | `Technical Writer` | 開發者文件、API 文件 | 🟡 中 | 候選 |

---

## 評比紀錄

<!-- 格式：
### agent-name
- **來源**：用戶自定義 / agency-agents / SDK 內建
- **任務**：做了什麼
- **呼叫方式**：subagent_type 或本地 agent 名稱
- **效果**：實際產出描述
- **優點**：
- **限制**：
- **評分**：效果 ⭐x / 省時 ⭐x
- **適合場景**：
- **驗證日期**：
-->
