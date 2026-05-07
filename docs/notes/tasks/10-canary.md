# Task 10：部署監控

**對應 action-plan**：#10  
**工具**：`canary` skill（gstack）

---

## Prompt（複製貼入新對話）

```
使用 canary skill（gstack）對 mmm-demo 進行健康檢查。
Streamlit app 在本機運行：http://localhost:8501

目標：
- --quick 模式：5 頁單次健康檢查
- 與 .gstack/benchmark-reports/baselines/baseline.json 對比
- 截圖佐證 3 頁以上
- 確認無 HTTP 錯誤、無效能回歸

將工具效果填入 docs/notes/tools/skills-eval.md 評比紀錄。
將本次改動填入 docs/notes/mmm-demo/iterations.md Iteration 10（對應 action-plan #10）。
```

---

## 完成條件

- [x] 5 頁全部 HTTP 200
- [x] 與 baseline 比對（無 2x 以上效能回歸）
- [x] 截圖佐證（3 張）
- [x] canary report JSON 儲存
- [x] skills-eval.md 有填入評比紀錄
- [x] iterations.md Iteration 10 有填入

## Canary 結果（2026-05-07）

**狀態：HEALTHY / 0 alerts**

| 頁面 | 結果 | load |
|------|------|------|
| 首頁 | HEALTHY（cold-start） | 751ms |
| 資料總覽 | HEALTHY | 38ms |
| 模型擬合 | HEALTHY | 27ms |
| 頻道貢獻 | HEALTHY | 25ms |
| 預算最佳化 | HEALTHY | 26ms |

## 完成後

→ 前往 [Task 11](11-retro.md)
