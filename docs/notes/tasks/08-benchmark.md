# Task 08：效能基準

**對應 action-plan**：#8  
**工具**：`benchmark` skill（gstack）

---

## Prompt（複製貼入新對話）

```
使用 benchmark skill（gstack）對 streamlit/mmm-demo 進行效能基準測試。
Streamlit app 已在本機運行：http://localhost:8501

目標：
- 測量全部 5 頁的 load time（dns/tcp/ttfb/domReady/load）
- 建立 baseline JSON 供後續版本比較
- 確認所有頁面 < 200ms（本機環境）
- 截圖佐證

將工具效果填入 docs/notes/tools/skills-eval.md 評比紀錄。
將本次改動填入 docs/notes/mmm-demo/iterations.md Iteration 8（對應 action-plan #8）。
```

---

## 完成條件

- [x] 5 頁效能數據收集（有數據佐證，非估算）
- [x] baseline.json 儲存至 `.gstack/benchmark-reports/baselines/`
- [x] 所有頁面 total load < 200ms 確認
- [x] skills-eval.md 有填入評比紀錄
- [x] iterations.md Iteration 8 有填入

## 基準數據（2026-05-07）

| 頁面 | total |
|------|-------|
| 首頁 | 41ms |
| 資料總覽 | 58ms |
| 模型擬合 | 69ms |
| 頻道貢獻 | 42ms |
| 預算最佳化 | 43ms |
| **平均** | **51ms** |

## 完成後

→ 前往 [Task 09](09-document-release.md)
