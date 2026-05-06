# Task 06：E2E 測試

**對應 action-plan**：#6  
**工具**：`e2e-runner` agent（用戶自定義）+ `Evidence Collector` agent（agency-agents）

---

## Prompt（複製貼入新對話）

```
使用 e2e-runner agent 跑 streamlit/mmm-demo 的關鍵用戶流程測試。
覆蓋 4 個頁面：資料總覽 → 模型擬合 → 頻道貢獻 → 預算最佳化。
用 Evidence Collector agent 驗收，要求截圖佐證每個頁面可正常運作。
將工具效果填入 docs/notes/tools/agents-eval.md 評比紀錄。
將本次改動填入 docs/notes/mmm-demo/iterations.md Iteration 6（對應 action-plan #6）。
```

---

## 完成條件

- [ ] 4 頁流程截圖齊全
- [ ] 無 uncaught exception
- [ ] agents-eval.md 有填入評比紀錄

## 完成後

→ 前往 [Task 07](07-deploy.md)
