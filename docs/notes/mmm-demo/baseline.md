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

（執行 Step 1 後填入）
