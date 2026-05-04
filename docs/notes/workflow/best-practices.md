# 最佳工作流紀錄

從實驗中累積出的有效工具組合。每條都需要實際驗證才能從「待驗證」移到「已驗證」。

---

## 已驗證工作流

### 安全掃描選擇策略
- **適用場景**：每次 commit/PR 前決定用哪個掃描工具
- **步驟**：
  1. 日常 commit → `security-review` skill（速度快，PR diff 導向，signal 高）
  2. 月度 or 部署前 → `cso --diff`（14-phase 全覆蓋，OWASP+STRIDE）
- **效果評分**：⭐⭐⭐⭐⭐
- **發現日期**：2026-05-04

<!-- 格式：
### 工作流名稱
- **適用場景**：
- **步驟**：
  1. 工具 A → 產出
  2. 工具 B → 產出
- **效果評分**：⭐x
- **發現日期**：
-->

---

## 待驗證假設

- [ ] `refactor-clean` → `python-review` 的順序是否比反過來更有效率？
- [ ] gstack `review` 比內建 `python-review` 找到更多 production bug？
- [x] gstack `cso` 的 OWASP+STRIDE 雙框架比內建 `security-review` 覆蓋更廣？→ 框架更廣，但本專案結論一致，日常用 `security-review` 足夠
- [ ] `Explore` agent 先做 baseline 分析再 refactor，是否比直接 refactor 更精準？
- [ ] `plan` → `tdd-workflow` → `code-review` 流水線是否比直接實作收斂更快？
- [ ] 雙 agent 並行（本地 + agency-agents 同一任務）是否比單一 agent 更準確？
- [ ] `Evidence Collector` agent 驗收是否有效阻止 Claude 幻想完成任務？
- [ ] gstack `autoplan`（CEO+Design+Eng 三角審查）對 Streamlit demo 是否過重？

---

## 工具對比實驗清單

同一任務用兩個工具跑，記錄差異：

| 任務 | 工具 A | 工具 B | 對比目標 | 狀態 |
|------|--------|--------|---------|------|
| Code review | `python-review`（內建） | `review`（gstack） | 發現問題深度與數量 | 待驗證 |
| 安全掃描 | `security-review`（內建） | `cso`（gstack） | OWASP 覆蓋範圍 | 待驗證 |
| 重構 | `refactor-clean` skill（內建） | `refactor-cleaner` agent（本地） | 產出品質與速度 | 待驗證 |
| Agent review | `code-reviewer`（本地） | `Code Reviewer`（agency-agents） | 角色化設定的影響 | 待驗證 |
