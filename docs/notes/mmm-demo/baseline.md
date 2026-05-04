# MMM-Demo MVP 基準快照

**日期**：2026-05-04
**狀態**：MVP 已可運行

## 如何收集已知問題

執行 Step 1 的 prompt（見 [README.md](../README.md)），讓 Claude 讀完所有元件後填入下方「已知問題」欄。

---

## 頁面清單

| 頁面 | 檔案 | 功能 |
|------|------|------|
| 主頁 | `app.py` | 導覽入口 |
| 資料總覽 | `pages/01_資料總覽.py` | 資料視覺化 |
| 模型擬合 | `pages/02_模型擬合.py` | MMM 訓練 |
| 頻道貢獻 | `pages/03_頻道貢獻.py` | ROAS 分析 |
| 預算最佳化 | `pages/04_預算最佳化.py` | 預算配置 |

## 元件

| 元件 | 檔案 | 說明 |
|------|------|------|
| MMM 封裝 | `components/mmm_runner.py` | 模型執行邏輯 |
| 圖表 | `components/charts.py` | 圖表函數 |
| AI 分析 | `components/ai_analysis.py` | Claude API 整合 |
| 進度條 | `components/progress.py` | 訓練進度顯示 |
| 字型設定 | `components/matplotlib_config.py` | 中文字型 |

## 品質指標（起點）

| 指標 | 現況 | 目標 | 量測方式 |
|------|------|------|---------|
| 單元測試覆蓋率 | 0% | 80%+ | `pytest --cov` |
| E2E 測試 | 無 | 關鍵流程覆蓋 | Playwright / `e2e-runner` agent |
| 錯誤處理 | 基本 | 完整 | code review 發現的未處理例外數 |
| 部署方式 | 本地手動 | 可一鍵部署 | 可用單一指令從零啟動 |

## 已知問題

| 優先序 | 問題 | 檔案 | 為何重要 |
|--------|------|------|---------|
| 1 | API 呼叫無 try/except，任何網路錯誤或 key 失效直接把 traceback 炸到 UI | `components/ai_analysis.py`（`analyze_roas_with_llm`、`analyze_fit_with_llm`） | 使用者體驗直接斷掉，且無法區分「模型問題」和「API 問題」 |
| 2 | 讀 CSV 用相對路徑 `"data/mock_cgp_data.csv"`，從非 app 根目錄執行就爆 | `components/mmm_runner.py`（`load_sample_data`，第 56 行） | `SAVE_PATH` 已用 `os.path.dirname(__file__)` 正確處理，但這裡沒有，造成不一致且部署會失敗 |
| 3 | CSS 用 `nth-child(4/5)` 鎖定頁面，新增或調換頁面順序會靜默鎖錯頁 | `components/progress.py`（第 49–60 行） | 鎖錯不報錯，只能靠人工視覺確認，維護風險高 |
