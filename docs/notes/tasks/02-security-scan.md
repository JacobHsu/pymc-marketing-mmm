# Task 02：安全掃描

**對應 action-plan**：#2  
**工具**：`security-review` skill（內建）vs `cso` skill（gstack）  
**對比實驗**：兩者 OWASP 覆蓋範圍差異

---

## Prompt（複製貼入新對話）

```
使用 security-review skill 掃描 streamlit/mmm-demo/components/ai_analysis.py 的 API key 處理方式。
再用 cso skill（gstack）做同樣的掃描。
比較兩者發現的差異，填入 docs/notes/tools/skills-eval.md 評比紀錄。
將本次改動填入 docs/notes/mmm-demo/iterations.md Iteration 2（對應 action-plan #2）。
```

---

## 完成條件

- [ ] 無 hardcode API key
- [ ] `.env` 防護確認
- [ ] 兩工具對比結果已填入 skills-eval.md
- [ ] iterations.md Iteration 2 有填入

## 完成後

→ 決定日常安全掃描用哪一個，記到 [best-practices.md](../workflow/best-practices.md)，前往 [Task 03](03-unit-tests.md)
