# 最佳工作流紀錄

從實驗中累積出的有效工具組合。每條都需要實際驗證才能從「待驗證」移到「已驗證」。

---

## 已驗證工作流

### 完整產品化流水線（6 task 實驗總結）

> 對一個現有 Streamlit demo 做完整品質提升，從重構到部署，依序執行以下工作流。

| 順序 | 工作 | 工具 | 效果 |
|------|------|------|------|
| 1 | 重構 + Code Review | `refactor-clean` → `python-review` | 函數縮短、型別補齊、死碼清除 |
| 2 | 安全掃描 | `security-review`（日常）/ `cso`（月度） | 無洩漏風險確認 |
| 3 | 單元測試 | `tdd-workflow` | 31 tests，testable 函數 100% 覆蓋 |
| 4 | UI 審查 | `design-review`（gstack） | 截圖驅動，發現 2 個 HIGH 問題並修復 |
| 5 | E2E 測試 | `e2e-runner` agent | 15 tests，覆蓋 5 頁核心流程 |
| 6 | 本機啟動腳本 | 手動建 `run.ps1` | 3 行指令合成 1 行 |

**原則**：先清再建 → 先安全再功能 → 先單元再 E2E → 先本地再部署

---

### 重構工作流
- **適用場景**：整理舊模組，移除死碼、抽取重複邏輯
- **步驟**：
  1. `refactor-clean` skill → 死碼分級（SAFE/CAUTION/DANGER），指引刪除與抽 helper
  2. `python-review` skill → 補型別標注、抓風格問題
- **注意**：vulture 60% 信心誤報需 grep 人工確認
- **效果評分**：⭐⭐⭐⭐
- **發現日期**：2026-05-04

### 安全掃描選擇策略
- **適用場景**：每次 commit/PR 前決定用哪個掃描工具
- **步驟**：
  1. 日常 commit → `security-review` skill（速度快，PR diff 導向，signal 高）
  2. 月度 or 部署前 → `cso --diff`（14-phase 全覆蓋，OWASP+STRIDE）
- **效果評分**：⭐⭐⭐⭐⭐
- **發現日期**：2026-05-04

### 單元測試工作流（Python + mock）
- **適用場景**：為純函數、資料處理管線建立測試
- **步驟**：
  1. `tdd-workflow` skill → RED→GREEN→REFACTOR 流程
  2. mock 策略：`patch` import-inside-function 路徑，xarray chain 用 `MagicMock` + `side_effect`
- **注意**：Windows 環境用 conda env 的 Python 可執行檔直接呼叫，避免 cp950 編碼問題
- **效果評分**：⭐⭐⭐⭐
- **發現日期**：2026-05-04

### UI 審查工作流
- **適用場景**：UI 改動後視覺驗收，或新頁面上線前 UX 問題排查
- **步驟**：
  1. `design-review` skill（gstack）→ 截圖 + 逐頁分析
  2. 問題分級 BLOCKER/HIGH/LOW，針對 HIGH 以上立即修復
- **注意**：截圖路徑需在 `Temp` 或專案目錄下；`$B js` 可讀取實際 DOM 確認 href 值
- **效果評分**：⭐⭐⭐⭐⭐
- **發現日期**：2026-05-04

### E2E 測試工作流
- **適用場景**：核心頁面導航流程、鎖定行為、CSS 驗證
- **步驟**：
  1. `e2e-runner` agent → 全程自主產出測試、執行、修復、回報
  2. Streamlit SPA 需 `networkidle` + 額外 wait 才能正確截圖
- **注意**：MCMC 流程需 pre-fitted fixture（`.nc` 檔）才能解鎖完整 E2E 測試
- **效果評分**：⭐⭐⭐⭐⭐
- **發現日期**：2026-05-04

<!-- 格式：
### 工作流名稱
- **適用場景**：
- **步驟**：
  1. 工具 A → 產出
  2. 工具 B → 產出
- **效果評分**：⭐x
- **發現日期**：
-->

---

## 待驗證假設

- [ ] `refactor-clean` → `python-review` 的順序是否比反過來更有效率？
- [ ] gstack `review` 比內建 `python-review` 找到更多 production bug？
- [x] gstack `cso` 的 OWASP+STRIDE 雙框架比內建 `security-review` 覆蓋更廣？→ 框架更廣，但本專案結論一致，日常用 `security-review` 足夠
- [ ] `Explore` agent 先做 baseline 分析再 refactor，是否比直接 refactor 更精準？
- [ ] `plan` → `tdd-workflow` → `code-review` 流水線是否比直接實作收斂更快？
- [ ] 雙 agent 並行（本地 + agency-agents 同一任務）是否比單一 agent 更準確？
- [ ] `Evidence Collector` agent 驗收是否有效阻止 Claude 幻想完成任務？
- [ ] gstack `autoplan`（CEO+Design+Eng 三角審查）對 Streamlit demo 是否過重？

---

## 工具對比實驗清單

同一任務用兩個工具跑，記錄差異：

| 任務 | 工具 A | 工具 B | 對比目標 | 狀態 |
|------|--------|--------|---------|------|
| Code review | `python-review`（內建） | `review`（gstack） | 發現問題深度與數量 | 待驗證 |
| 安全掃描 | `security-review`（內建） | `cso`（gstack） | OWASP 覆蓋範圍 | 待驗證 |
| 重構 | `refactor-clean` skill（內建） | `refactor-cleaner` agent（本地） | 產出品質與速度 | 待驗證 |
| Agent review | `code-reviewer`（本地） | `Code Reviewer`（agency-agents） | 角色化設定的影響 | 待驗證 |
