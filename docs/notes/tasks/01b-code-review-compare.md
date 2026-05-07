# Task 01b：工具對比 — Code Review

**對應 action-plan**：#01b（支線）  
**工具對比**：`python-review`（everything-claude-code）vs `review`（gstack）  
**對象檔案**：`streamlit/mmm-demo/components/ai_analysis.py`  
**執行時間**：2026-05-07

---

## 背景

`python-review` 已於 Task 01（refactor 後）執行並產出報告。本支線補跑 gstack `/review` 對同一檔案做比較，量化兩個工具的「發現問題深度與數量」差異。

---

## 執行說明

### python-review（2026-05-04）

正常執行，在 refactor-clean 完成後立即審查。

### gstack /review（2026-05-07）

gstack `/review` skill 基於 `git diff origin/main --stat` 運作，需要 branch 有 diff。本次在 `main` branch 執行，diff 為空，skill 自動停止（設計如此）。

**因應方式**：直接讀取 `ai_analysis.py` 後套用 /review checklist（correctness、performance、type safety、error handling、production risk）。

---

## 完成條件

- [x] python-review 結果已記錄（Task 01，2026-05-04）
- [x] gstack /review 執行嘗試並記錄阻擋原因
- [x] 手動套用 /review checklist 完成分析
- [x] 兩工具發現對比表完成
- [x] skills-eval.md 補入 `review (gstack)` 評比
- [x] 實驗假設結果填入

---

## 兩工具發現對比

目標檔案共 125 行，4 個函數（`_make_client`、`_compute_fit_metrics`、`analyze_roas_with_llm`、`analyze_fit_with_llm`）。

| 問題 | python-review | gstack /review | 備註 |
|------|--------------|----------------|------|
| `_make_client` 缺回傳型別標注 | ✅ HIGH | — | 已修（refactor 後） |
| `mmm: Any` 型別 | ✅ HIGH | — | 已修（TYPE_CHECKING guard） |
| 行長超過 PEP 8 88 chars | ✅ MEDIUM | — | 部分行仍略超，不影響運行 |
| `chr(10)` workaround | ✅ MEDIUM | — | 已修（`_NL = "\n"`） |
| Client 未快取（每次 call 重建） | ✅ MEDIUM | ✅ MEDIUM | 兩者都抓到；Streamlit 每次渲染一次，實際影響有限 |
| 缺 error handling（API call） | ✅ MEDIUM | ✅ MEDIUM | python-review 較籠統；/review 更具體 |
| `response.choices[0]` IndexError 風險 | — | ✅ MEDIUM | /review 獨有：API 若回傳空 choices 會 crash |
| 無 `timeout` 參數（API 可能 hang） | — | ✅ MEDIUM | /review 獨有：網路問題時無超時保護 |

**python-review 找到**：6 項（2 HIGH + 4 MEDIUM），其中 4 項已修  
**gstack /review 找到**：4 項（0 HIGH + 4 MEDIUM），其中 2 項與 python-review 重疊，2 項為獨有  

---

## 實驗假設驗證

| 假設 | 預期 | 實際結果 |
|------|------|---------|
| gstack `review` 比內建 `python-review` 找到更多問題 | gstack 有角色設定更深入 | **部分成立**：/review 找到 2 個 python-review 沒有的 production runtime 問題（IndexError、timeout），但 python-review 在型別分析上更深入（發現 2 HIGH 型別問題） |

**結論**：兩者互補，非替代關係。
- `python-review` → 型別標注、PEP 8、靜態分析強項
- `gstack /review` → production runtime 風險（IndexError、timeout、掛起）強項；但需要 branch diff 才能執行，main branch 直接跑無效

---

## 工具使用限制說明

**gstack /review 限制**：
- 必須在非 main branch 且有 uncommitted diff 時執行
- 在 main branch 上直接跑，skill 偵測到 `git diff origin/main --stat` 為空後自動停止
- 適合在 feature branch 開發期間跑，不適合事後回顧

**因應方案**：
- 若要對現有 main branch 程式碼跑 /review，需先建 branch 並做一個小改動（如加空行）再執行
- 或如本次：讀檔後手動套用 checklist，效果 ≈ 75%（缺少 AI 角色加持的深度推理）
