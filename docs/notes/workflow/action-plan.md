# 行動清單

> 從候選清單中選出、排好優先序的執行計畫。  
> 候選清單見 [skills-eval.md](../tools/skills-eval.md) · [agents-eval.md](../tools/agents-eval.md)

## 排序依據

| 原則 | 說明 |
|------|------|
| **先清再建** | 結構亂的程式難以測試，重構先於測試 |
| **先安全再功能** | API key 處理不當會造成資安風險，早掃早好 |
| **先單元再 E2E** | 單元測試快速反饋，E2E 成本高留後 |
| **先 QA 再自動化** | 真瀏覽器 QA 驗收在 Playwright 自動化前 |
| **先本地再部署** | 本地品質不穩定，部署只是放大問題 |
| **編號即順序** | 必作主線重新編號；可選支線用字母（如 04b） |

---

## 行動清單

| # | 任務 | 工具 | 類型 | 驗證方式 | 狀態 |
|---|------|------|------|---------|------|
| 0 | 確認起點 | — | 基準 | baseline 快照 | 完成 |
| 1 | 重構 `ai_analysis.py` | `refactor-clean` skill + `python-review` skill | 重構 | 函數長度 < 50 行、無死碼 | 完成 |
| 2 | 安全掃描 | `security-review` skill vs `cso` skill（gstack） | 安全 | 無 hardcode key、有 `.env` 防護 | 完成 |
| 3 | 單元測試 | `tdd-workflow` skill | 測試 | coverage ≥ 80% | 完成 |
| 4 | UI 審查 | `design-review` skill（gstack） | UI | 有截圖佐證，列出問題清單 | 完成 |
| 5 | 真瀏覽器 QA | `qa` skill（gstack） | 測試 | 5 頁流程截圖，無 uncaught exception | 待開始 |
| 6 | E2E 自動化測試 | `e2e-runner` agent | 測試 | 15 個測試全 PASSED | 完成 |
| 7 | 部署設定 | `setup-deploy` / `ship` skill（gstack） | 部署 | 可一鍵啟動 | 完成 |
| 8 | 效能基準 | `benchmark` skill（gstack） | 效能 | 頁面載入時間、Core Web Vitals 基準建立 | 待開始 |
| 9 | 文件更新 | `document-release` skill（gstack） | 文件 | README、pages 說明與程式碼同步 | 待開始 |
| 10 | 部署監控 | `canary` skill（gstack） | 監控 | Streamlit Cloud 無 console 錯誤、無頁面失敗 | 待開始 |
| 11 | 回顧 | `retro` skill（gstack） | 回顧 | 整輪工具效果總結、最佳工作流萃取 | 待開始 |

---

## 支線（可選）

| # | 任務 | 工具 | 類型 | 狀態 |
|---|------|------|------|------|
| 01b | 工具對比：code review | `review` skill（gstack） vs `python-review` | 重構 | 待開始 |
| 04b | UI 風格重做 | `design-shotgun` skill（gstack） | UI | 完成 |

---

## 工具對比實驗

同一任務用兩個工具跑，記錄差異：

| 任務 | 工具 A | 工具 B | 對比目標 | 狀態 |
|------|--------|--------|---------|------|
| Code review | `python-review`（內建） | `review`（gstack） | 發現問題的深度與數量 | 待開始（見支線 01b） |
| 安全掃描 | `security-review`（內建） | `cso`（gstack） | OWASP 覆蓋範圍 | 完成 |
| 重構 | `refactor-clean`（內建） | `refactor-cleaner` agent（本地） | 產出品質與速度 | 待開始 |
