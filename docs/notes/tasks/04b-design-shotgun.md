# Task 04b：UI 風格重做

**對應 action-plan**：#4b（04 進階）  
**工具**：`design-shotgun` skill（gstack）→ CSS 實作 → `design-review` 驗收

---

## 背景

Task 04 的 `design-review` 已找出導航與 CSS 鎖頁問題並修復。  
本 task 進一步解決「明顯 AI 生成感」：大量 emoji、配色過飽和、佈局鬆散。

目標：讓介面看起來像正常的資料分析工具，而非 AI demo。

## Prompt（複製貼入新對話）

```
使用 design-shotgun skill（gstack）對 streamlit/mmm-demo/ 產出設計方向變體。
目標：移除 AI 感（emoji、過飽和配色、鬆散佈局），改為專業資料分析工具風格。
選定方向後實作 CSS 覆寫，不需要換元件庫。
完成後截圖驗收，確認改動有效。
將工具效果填入 docs/notes/tools/skills-eval.md 評比紀錄。
將本次改動填入 docs/notes/mmm-demo/iterations.md Iteration 4b。
```

---

## 完成條件

- [ ] design-shotgun 產出至少 2 個設計方向
- [ ] 選定方向已實作（CSS 覆寫或元件調整）
- [ ] before/after 截圖對比
- [ ] emoji 數量明顯減少
- [ ] skills-eval.md 有填入 design-shotgun 評比紀錄
- [ ] iterations.md Iteration 4b 有填入

## 完成後

→ 前往 [Task 05](05-e2e-tests.md)（E2E 驗收新 UI）
