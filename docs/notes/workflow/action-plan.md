# 行動清單

> 從候選清單中選出、排好優先序的執行計畫。  
> 候選清單見 [skills-eval.md](../tools/skills-eval.md) · [agents-eval.md](../tools/agents-eval.md)

## 排序依據

| 原則 | 說明 |
|------|------|
| **先清再建** | 結構亂的程式難以測試，重構先於測試 |
| **先安全再功能** | API key 處理不當會造成資安風險，早掃早好 |
| **先單元再 E2E** | 單元測試快速反饋，E2E 成本高留後 |
| **先本地再部署** | 本地品質不穩定，部署只是放大問題 |

---

## 行動清單

| # | 任務 | 工具 | 類型 | 驗證方式 | 狀態 |
|---|------|------|------|---------|------|
| 1 | 整理 `ai_analysis.py` 結構 | `refactor-clean` skill + `python-review` skill | 重構 | 函數長度 < 50 行、無死碼 | 待開始 |
| 2 | 掃描 API key 處理安全性 | `security-review` skill vs `cso` skill（gstack） | 安全 | 無 hardcode key、有 `.env` 防護 | 待開始 |
| 3 | 建立 `mmm_runner.py` 單元測試 | `tdd-workflow` skill | 測試 | coverage ≥ 80% | 待開始 |
| 4 | UI 一致性審查 | `design-review` skill（gstack） | UI | 有截圖佐證，列出問題清單 | 待開始 |
| 5 | E2E 關鍵流程測試 | `e2e-runner` agent | 測試 | 4 頁流程可完整跑通 | 待開始 |
| 6 | 部署設定 | `setup-deploy` / `ship` skill（gstack） | 部署 | 可一鍵啟動，非本地手動 | 待開始 |

---

## 工具對比實驗（額外）

同一任務用兩個工具跑，記錄差異：

| 任務 | 工具 A | 工具 B | 對比目標 |
|------|--------|--------|---------|
| Code review | `python-review`（內建） | `review`（gstack） | 發現問題的深度與數量 |
| 安全掃描 | `security-review`（內建） | `cso`（gstack） | OWASP 覆蓋範圍 |
| 重構 | `refactor-clean`（內建） | `refactor-cleaner` agent（本地） | 產出品質與速度 |
