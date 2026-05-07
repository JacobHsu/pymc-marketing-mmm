# Task 09：文件更新

**對應 action-plan**：#9  
**工具**：`document-release` skill（gstack）

---

## Prompt（複製貼入新對話）

```
使用 document-release skill（gstack）同步 mmm-demo 的文件。

目標：
- 審查 streamlit/mmm-demo/README.zh-TW.md 是否與程式碼同步（目錄結構、頁面標籤）
- 審查 .claude/CLAUDE.md 路徑是否正確
- 確認 best-practices.md 的流水線步驟覆蓋所有已完成 task
- 跨文件任務狀態（action-plan vs notes/README）一致性

將工具效果填入 docs/notes/tools/skills-eval.md 評比紀錄。
將本次改動填入 docs/notes/mmm-demo/iterations.md Iteration 9（對應 action-plan #9）。
```

---

## 完成條件

- [x] README.zh-TW.md 目錄結構正確（含 run.ps1、ui_helpers.py、tests/）
- [x] .claude/CLAUDE.md 路徑指向正確位置
- [x] best-practices.md 流水線反映 9 個 task
- [x] 跨文件任務狀態一致
- [x] skills-eval.md 有填入評比紀錄
- [x] iterations.md Iteration 9 有填入

## 完成後

→ 前往 [Task 10](10-canary.md)
