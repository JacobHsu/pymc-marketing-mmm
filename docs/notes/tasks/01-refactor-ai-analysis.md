# Task 01：重構 ai_analysis.py

## 本次實驗工具

| 角色 | 工具 | 來源 |
|------|------|------|
| 主要實驗 | `refactor-clean` skill | 內建 |
| 審查驗收 | `python-review` skill | 內建 |
| 對比組 | `refactor-cleaner` agent | 用戶自定義 |

> 對比問題：`refactor-clean` skill 和 `refactor-cleaner` agent 同樣做重構，產出品質和速度有何差異？

---

## Prompt（複製貼入新對話）

```
使用 refactor-clean skill 整理 streamlit/mmm-demo/components/ai_analysis.py。
完成後用 python-review skill 審查結果。
將兩個工具的效果（優點、限制、評分）填入 docs/notes/tools/skills-eval.md 的評比紀錄。
將本次改動填入 docs/notes/mmm-demo/iterations.md Iteration 1（對應 action-plan #1）。
```

---

## 完成條件

- [ ] `ai_analysis.py` 函數長度 < 50 行
- [ ] 無死碼
- [ ] skills-eval.md 有填入評比紀錄
- [ ] iterations.md Iteration 1 有填入

## 完成後

→ 更新 README 進度表，前往 [Task 02](02-security-scan.md)
