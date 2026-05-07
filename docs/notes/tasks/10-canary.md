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

## Cloud Canary 結果（2026-05-07）

**目標**：https://pymc-marketing-mmm.streamlit.app/  
**狀態：HEALTHY / 0 CRITICAL alerts**

| 頁面 | domReady | 備注 |
|------|---------|------|
| 首頁 | 5499ms | Streamlit Cloud container 冷啟動 |
| 資料總覽 | 536ms | ttfb ≈ 350ms（跨洲 CDN） |
| 模型擬合 | 493ms | 正常 |
| 頻道貢獻 | 471ms | 正常 |
| 預算最佳化 | 450ms | 正常 |

**與 localhost baseline 差異說明**：
- Warm 頁 450–536ms vs localhost 25–58ms（差 ~10x）為預期：Streamlit Cloud 在台灣無 edge node，TTFB ≈ 350ms 是跨洋 RTT
- 首頁 5499ms 為 container cold-start，是 Streamlit Community Cloud 免費方案已知行為（idle 後 container 需重啟）
- 截圖佐證：`.gstack/canary-reports/screenshots/cloud/canary-cloud-{home,data,channel}.png`

## 完成後

→ 前往 [Task 11](11-retro.md)
