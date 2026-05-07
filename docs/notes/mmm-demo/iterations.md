# 迭代紀錄

每次迭代記錄：用了哪些 Claude Code 工具、改了什麼、品質如何變化。  
對應 action-plan 任務編號見 [workflow/action-plan.md](../workflow/action-plan.md)。

---

<!-- 格式：
## Iteration N — YYYY-MM-DD（action-plan #N）

**目標**：這次迭代要解決什麼

### 使用工具
| 工具 | 來源 | 類型 | 用途 |
|------|------|------|------|
| xxx | 內建/gstack/agency-agents | skill/agent | 做了什麼 |

### 改動
- 檔案：改了什麼

### 品質變化
| 指標 | Before | After |
|------|--------|-------|
| xxx | | |

### 心得
工具效果、踩坑、下次改進方向
-->

## Iteration 1 — 2026-05-04（action-plan #1）

**目標**：整理 `ai_analysis.py`，移除死碼、抽取重複邏輯，驗證 `refactor-clean` + `python-review` 組合

### 使用工具
| 工具 | 來源 | 類型 | 用途 |
|------|------|------|------|
| `refactor-clean` | everything-claude-code | skill | 死碼偵測（vulture）、分類、抽 helper |
| `python-review` | everything-claude-code | skill → agent | 型別標注、風格、安全審查 |

### 改動
- `components/ai_analysis.py`：移除死碼 `channel_cols` 參數；抽出 `_make_client()`、`_compute_fit_metrics()` helper；函數長度從最長 68 行降至 < 50 行；補齊 `_make_client` 回傳型別與 `mmm` 參數型別；修正 `chr(10)` 為 `_NL` 常數
- `pages/03_頻道貢獻.py`：移除對應的 `channel_cols=channel_cols` 呼叫端參數

### 品質變化
| 指標 | Before | After |
|------|--------|-------|
| 最長函數行數 | 68 行 | 42 行 |
| 死碼（vulture 100%）| 1 個（`channel_cols`）| 0 |
| 重複邏輯 | OpenAI client 建立重複 2 次 | 統一到 `_make_client` |
| 型別標注完整度 | 不完整（`mmm: Any`、無回傳型別） | HIGH 問題全修 |

### 心得
- `refactor-clean` + `python-review` 串接效果好：前者指引結構清理，後者補抓型別漏洞
- vulture 的 60% 信心誤報需要人工用 grep 確認，不能盲目信任
- `python-review` 的 MEDIUM「client 未快取」在 Streamlit 場景不算真問題（每次渲染一次 API call），需依情境判斷

## Iteration 2 — 2026-05-04（action-plan #2）

**目標**：驗證 `security-review` vs `cso` 安全掃描覆蓋差異，確認 `mmm-demo` 無明顯安全問題

### 使用工具
| 工具 | 來源 | 類型 | 用途 |
|------|------|------|------|
| `security-review` | Claude Code 原生 | skill → agent | PR diff 導向安全掃描 |
| `cso` | gstack | skill | 全相位安全掃描（14 phases，OWASP+STRIDE） |

### 改動
- 無程式碼改動（純掃描任務）
- `docs/notes/tools/skills-eval.md`：新增 `security-review`、`cso` 評比紀錄
- `docs/notes/workflow/best-practices.md`：新增日常安全掃描工作流決策

### 品質變化
| 指標 | Before | After |
|------|--------|-------|
| Hardcode API key | 未確認 | 已確認無 |
| .env 保護 | 未確認 | 已確認 gitignored |
| git history 洩漏 | 未確認 | 已確認無 |
| LLM output XSS | 未確認 | 已確認無（st.markdown 預設安全） |

### 心得
- 兩工具結論完全一致：無高信心弱點
- `security-review`（PR diff 導向）速度更快，日常使用足夠
- `cso` 的 14-phase 框架對純本地 Streamlit 有點過重，但 STRIDE 威脅模型在架構規劃時有參考價值
- **決策**：日常用 `security-review`；每月或部署前用 `cso --diff`

## Iteration 3 — 2026-05-04（action-plan #3）

**目標**：為 `mmm_runner.py` 的純函數建立單元測試，目標覆蓋率 80%+

### 使用工具
| 工具 | 來源 | 類型 | 用途 |
|------|------|------|------|
| `tdd-workflow` | everything-claude-code | skill | 指引 RED→GREEN→REFACTOR 流程 |
| `python-reviewer` agent | everything-claude-code | agent | 確認 test 寫法與 mock 策略 |

### 改動
- 新增 `streamlit/mmm-demo/tests/__init__.py`（空檔，讓 pytest 識別 package）
- 新增 `streamlit/mmm-demo/tests/conftest.py`（加入 mmm-demo 根目錄至 sys.path）
- 新增 `streamlit/mmm-demo/tests/test_mmm_runner.py`（31 個測試，7 個 TestClass）
- 安裝 `pytest`、`pytest-cov` 至 conda env `pymc-marketing-dev`

### 品質變化
| 指標 | Before | After |
|------|--------|-------|
| 單元測試數量 | 0 | 31（全部通過） |
| `mmm_runner.py` 覆蓋率 | 0% | 71% |
| testable 函數覆蓋率 | 0% | 100% |
| MCMC 函數（刻意排除） | — | 0%（需真實 PyMC 採樣，已於 docstring 標注） |

### 心得
- `tdd-workflow` 對 mock 策略指引有效：`MagicMock` 搭配 `sel_side_effect` 正確模擬 xarray idata chain
- Windows 環境下 `conda run` 有 cp950 編碼問題，需直接呼叫 conda env 的 Python 可執行檔
- 整體覆蓋率 71% 而非 80%，原因是 `build_mmm`、`fit_mmm`、`sample_posterior_predictive` 需要真實 MCMC 採樣，無法 mock；testable 函數達 100%
- HF Hub 下載路徑用 `patch("huggingface_hub.hf_hub_download")` 覆蓋，需注意 import-inside-function 的 mock 方式

## Iteration 4 — 2026-05-04（action-plan #4）

**目標**：對 mmm-demo 5 頁 UI 進行視覺稽核，找出並修復導航與可維護性問題

### 使用工具
| 工具 | 來源 | 類型 | 用途 |
|------|------|------|------|
| `design-review` | gstack | skill | 截圖驅動 UI 審查，發現 UX 與維護風險 |

### 改動
- `streamlit/mmm-demo/components/progress.py`：FINDING-002 — 將 CSS 鎖頁邏輯從 `li:nth-child(4/5)` 改為 `a[href*="/頻道貢獻"]`、`a[href*="/預算最佳化"]` 屬性選擇器，頁面順序調整時不再靜默鎖錯
- `streamlit/mmm-demo/pages/03_頻道貢獻.py`：FINDING-001 — 在鎖定警告後新增 `st.page_link("pages/02_模型擬合.py", ...)`，使用者不需回側邊欄即可導航
- `streamlit/mmm-demo/pages/04_預算最佳化.py`：同上

### 品質變化
| 指標 | Before | After |
|------|--------|-------|
| 鎖定頁面警告有無導航連結 | 無（使用者卡住） | 有（st.page_link 直接連到模型擬合） |
| CSS 鎖頁邏輯 | nth-child 位置依賴，頁面順序改動就壞 | href 屬性選擇器，穩定 |
| 導航 UX 流程完整性 | BLOCKER：鎖定頁面無出口 | 已修復 |

### 心得
- `design-review` 截圖驅動分析比純靜態分析有效：nth-child 問題在 code review 中可能被忽略，但截圖後一眼就能確認頁面順序
- `$B js` JavaScript 注入可讀取實際 DOM href 值，確認 Streamlit 使用未編碼中文字 href（如 `/頻道貢獻`），讓 CSS 屬性選擇器可以直接匹配
- `st.page_link` 是 Streamlit 原生多頁導航 API，比自製 `st.markdown` 連結更正確；`st.stop()` 前插入即生效
- Windows 環境 `$B` 截圖路徑白名單須注意：只接受 `Temp` 目錄或專案目錄

## Iteration 5 — 2026-05-04（action-plan #5）

**目標**：為 mmm-demo 4 個核心頁面流程建立 E2E 測試，覆蓋導航、鎖定行為、CSS 驗證

### 使用工具
| 工具 | 來源 | 類型 | 用途 |
|------|------|------|------|
| `e2e-runner` | Claude Code 內建 | agent | 撰寫並執行 Playwright E2E 測試 |

### 改動
- 新增 `streamlit/mmm-demo/tests/e2e/__init__.py`（空檔）
- 新增 `streamlit/mmm-demo/tests/e2e/test_navigation.py`（15 個測試，5 個 TestClass）

### 品質變化
| 指標 | Before | After |
|------|--------|-------|
| E2E 測試數量 | 0 | 15（全部 PASSED） |
| 覆蓋頁面 | 0 | 5（首頁、資料總覽、模型擬合、頻道貢獻鎖定、預算最佳化鎖定） |
| CSS lock 驗證 | 無 | 有（getComputedStyle 確認 pointer-events: none） |
| FINDING-001 回歸保護 | 無 | 有（test_goto_model_fitting_link_visible） |

### 心得
- `e2e-runner` 全程自主：產出測試、執行、修復 strict-mode 錯誤、回報結果，無需人工介入
- Streamlit React SPA 需要 `networkidle` + 額外 wait 才能正確截圖，headless Chrome `--screenshot` 旗標太早截圖；應直接用 Playwright API
- `pytest-cov` 對 browser-driven 測試回報 exit code 1 屬誤報，需在 pytest 設定排除或忽略
- MCMC 流程（模型擬合後的完整功能頁）是自動化 E2E 的天花板，需要另外設計 fixture（pre-fitted .nc 檔）才能解鎖

## Iteration 6 — 2026-05-06（action-plan #6）

**目標**：讓 mmm-demo 可用單一指令從零本機啟動，不再需要手動輸入三行指令

### 使用工具
| 工具 | 來源 | 類型 | 用途 |
|------|------|------|------|
| `setup-deploy` | gstack | skill | 原意為雲端部署設定，本次確認 app 已部署，改為建立本機啟動腳本 |

### 改動
- 新增 `streamlit/mmm-demo/run.ps1`：一鍵 activate 環境並啟動 Streamlit
- 更新 `streamlit/mmm-demo/README.zh-TW.md`：快速啟動改為 `.\run.ps1` 單行指令

### 品質變化
| 指標 | Before | After |
|------|--------|-------|
| 本機啟動步驟數 | 3 行（conda activate + cd + streamlit run） | 1 行（`.\run.ps1`） |
| 啟動文件說明 | 三行分開指令 | 單一腳本，任意目錄可執行 |

### 心得
- `setup-deploy` skill 預設導向雲端部署設定，對「已部署」的專案不直接適用；task 目標是本機啟動自動化，方向不同
- `run.ps1` 用 `$MyInvocation.MyCommand.Path` 取得腳本位置再 `Set-Location`，讓腳本從 repo 根目錄或 `streamlit/mmm-demo/` 執行結果相同
- Streamlit Cloud 部署說明已在 README 的「雲端部署」章節，不需額外文件

## Iteration 5 — 2026-05-07（action-plan #5）

**目標**：對 mmm-demo 5 頁 UI 進行真瀏覽器 QA，驗收 04b 設計重做後的 Material Icons 顯示與導航正確性

### 使用工具
| 工具 | 來源 | 類型 | 用途 |
|------|------|------|------|
| `qa` | gstack | skill | 真瀏覽器截圖、console 錯誤檢查、導航驗收 |

### 改動
- 無程式碼改動（純 QA 驗收，無 bug 需修復）
- 新增 `.gstack/qa-reports/screenshots/`：5 頁截圖（01-home、02-data-overview、03-model-fit、04-channel-contrib、05-budget-opt）

### 品質變化
| 指標 | Before | After |
|------|--------|-------|
| 04b UI 視覺驗收 | 無截圖佐證 | 5 頁截圖完整 |
| Material Icons 渲染確認 | 未驗證 | 全 5 個 icon 確認正確 |
| 導航連結（FINDING-001 回歸） | 未驗證 | 確認兩個鎖定頁均有「前往模型擬合」連結 |
| Console JS 錯誤 | 未知 | 無 uncaught exception（Streamlit 內建 404 屬已知行為） |
| 健康分數 | — | 95/100 |

### 心得
- `$B goto` 直接導航 Streamlit 子頁面後需等 3 秒，頁面才能完整渲染（React SPA 初始化時間）
- `$B snapshot -i -a` 在 Streamlit 多元素頁面觸發「matched multiple elements」，改用 `$B screenshot` 即可
- 404 錯誤（`/_stcore/health`、`/_stcore/host-config`）是 Streamlit 多頁 app 的已知行為：直接 `goto` 子頁面時，Streamlit 內部 fetch 會把頁面路徑拼入 URL，屬 Streamlit 框架問題，非我們程式碼的問題
- `$B js window.performance.getEntriesByType('resource')` 可精確定位 404 資源名稱，比肉眼看 console log 更快

## Iteration 4b — 2026-05-06（action-plan #4b）

**目標**：將 mmm-demo UI 從 emoji 風格升級為 Material Icons + C-style 企業設計，提升報告質感

### 使用工具
| 工具 | 來源 | 類型 | 用途 |
|------|------|------|------|
| `design-shotgun` | gstack | skill | 設計系統規劃 + 逐頁 icon 替換 + CSS 一致性 |

### 改動
- 新增 `streamlit/mmm-demo/components/ui_helpers.py`：`icon_title`、`icon_header`、`icon_subheader` HTML helper，用 Material Symbols Rounded 字型渲染圖示（`unsafe_allow_html`）
- `streamlit/mmm-demo/components/progress.py`：側邊欄進度步驟圖示從 emoji（✅▶️🔒）改為符號（✓ › —），移除標題 emoji
- `streamlit/mmm-demo/app.py`：`st.title` emoji → `icon_title("analytics", ...)`；三個 section header emoji → `icon_subheader(...)`
- `streamlit/mmm-demo/pages/01_資料總覽.py`：`st.title` → `icon_title("table_chart", ...)`；expander/button/page_link emoji 全換為 `:material/xxx:`
- `streamlit/mmm-demo/pages/02_模型擬合.py`：`st.title` → `icon_title("model_training", ...)`；button emoji → `:material/bolt:` / `:material/play_arrow:`
- `streamlit/mmm-demo/pages/03_頻道貢獻.py`：`st.title` → `icon_title("stacked_bar_chart", ...)`；button/page_link emoji 全換
- `streamlit/mmm-demo/pages/04_預算最佳化.py`：`st.title` → `icon_title("savings", ...)`；button emoji → `:material/search:`；loop 圖示從 emoji 改為 ASCII 箭頭（↑↓→）
- 新增 `docs/install/gstack.zh-tw.md`：gstack README 完整繁體中文翻譯

### 品質變化
| 指標 | Before | After |
|------|--------|-------|
| 頁面標題圖示 | emoji（📊💰⚙️） | Material Icons（svg 字型） |
| 按鈕圖示 | emoji（🚀🔍⚡） | `:material/xxx:` 原生語法 |
| section header 圖示 | emoji（🎯📝💡） | `icon_subheader()` HTML helper |
| 垂直置中 | — | flex + display:block 修正對齊 |
| 報告質感 | prototype 風格 | 企業匯報品質 |

### 心得
- Streamlit `st.title()` / `st.header()` / `st.subheader()` 不支援 `icon=` 參數，只能用 `unsafe_allow_html` 繞道
- Material Symbols Rounded 字型由 Streamlit 本地打包（woff2），不需 CDN；字型名稱 `"Material Symbols Rounded"` 從 Streamlit bundle 確認
- 垂直置中核心：用 `<div>` 而非 `<h1>/<h3>`（避免 heading 的 baseline 行為），icon span 加 `display:block`（消除 inline descender 空白）
- `st.button(icon=":material/xxx:")` 和 `st.page_link(icon=":material/xxx:")` 是唯一原生支援圖示的元件，其餘必須 HTML 注入

## Iteration 8 — 2026-05-07（action-plan #8）

**目標**：建立 mmm-demo 5 頁效能基準（baseline），記錄 load time 供後續迭代比較

### 使用工具
| 工具 | 來源 | 類型 | 用途 |
|------|------|------|------|
| `benchmark` | gstack | skill | 真瀏覽器效能測試、baseline JSON 建立 |

### 改動
- 新增 `.gstack/benchmark-reports/baselines/baseline.json`：5 頁效能基準數據
- 新增 `.gstack/benchmark-reports/screenshots/benchmark-home.png`：首頁截圖佐證

### 品質變化
| 指標 | Before | After |
|------|--------|-------|
| 效能基準 | 無 | 5 頁 baseline 建立（avg 51ms） |
| 最慢頁面 | 未知 | 模型擬合 69ms（含 MCMC state check） |
| 最快頁面 | 未知 | 首頁 41ms |
| 所有頁面 < 200ms | 未驗證 | ✓ 確認 |

### 效能數據（localhost）
| 頁面 | total | ttfb | domReady |
|------|-------|------|---------|
| 首頁 | 41ms | 2ms | 41ms |
| 資料總覽 | 58ms | 6ms | 58ms |
| 模型擬合 | 69ms | 8ms | 69ms |
| 頻道貢獻 | 42ms | 4ms | 42ms |
| 預算最佳化 | 43ms | 4ms | 42ms |

### 心得
- `$B perf` 是最快取得結構化效能數據的方法，dns/tcp/ssl/ttfb/domParse/domReady/load 一次輸出
- 模型擬合頁面（69ms）略慢於其他頁面，推測因為該頁會 check MCMC session state
- localhost 環境 dns/tcp 均為 0ms，ttfb 即為 Streamlit Python server 的純處理時間
- `$B eval` 多行 JS 在 Windows 環境有相容性問題（exit code 1），ResourceTiming entries 無法取得；可改用 `$B js` 語法或避開多行 JSON.stringify
- baseline 數據只有參考意義（本機開發環境），生產環境效能需另外量測

## Iteration 9 — 2026-05-07（action-plan #9）

**目標**：同步 iterations 4b–8 後的所有文件，確保 README、目錄結構、任務狀態跨文件一致

### 使用工具
| 工具 | 來源 | 類型 | 用途 |
|------|------|------|------|
| `document-release` | gstack | skill | 文件審查、factual 修正、跨文件一致性檢查 |

### 改動
- `streamlit/mmm-demo/README.zh-TW.md`：移除重複行；目錄結構加入 `run.ps1`、`components/progress.py`、`components/ui_helpers.py`、`tests/`；修正 AI expander 標籤（移除 🤖 emoji，與程式碼一致）
- `.claude/CLAUDE.md`：修正過時路徑（`sandbox/streamlit_demo/` → `streamlit/mmm-demo/`）
- `docs/notes/workflow/best-practices.md`：流水線從 6 步擴展至 9 步（加入 4b/5/8）；安全掃描對比狀態修正為「完成」
- `docs/notes/workflow/action-plan.md`：tasks 5/8 標記完成，task 9 更新為進行中

### 品質變化
| 指標 | Before | After |
|------|--------|-------|
| README 目錄結構準確度 | 缺少 3 個新元件 + tests/ | 完整（8 個檔案）|
| 過時路徑 | sandbox/streamlit_demo（不存在）| streamlit/mmm-demo（正確）|
| AI expander 標籤 | 🤖 AI 行銷洞察（emoji） | AI 行銷洞察（與程式碼一致）|
| 流水線步驟數 | 6 步 | 9 步（完整反映所有已完成 task）|
| 跨文件一致性 | task 5/8 狀態不一致 | 全部同步 |

### 心得
- `document-release` 的 auto-update vs ask-user 分類邏輯有效：明確 factual 錯誤直接修正，不詢問
- on main branch 直接工作時，PR body/title update 步驟可跳過（不阻塞流程）
- 跨文件狀態一致性（action-plan vs README vs best-practices）是最容易遺漏的 doc debt
- 需要 domain context 才能正確判斷哪些路徑是 stale，純靠 diff 不夠

## Iteration 10 — 2026-05-07（action-plan #10）

**目標**：對 mmm-demo localhost 執行 canary 快速健康檢查，與 Task 08 baseline 對比

### 使用工具
| 工具 | 來源 | 類型 | 用途 |
|------|------|------|------|
| `canary` | gstack | skill | 真瀏覽器健康檢查、baseline 比對、截圖佐證 |

### 改動
- 新增 `.gstack/canary-reports/2026-05-07-canary.json`：健康報告
- 新增 `.gstack/canary-reports/screenshots/canary-{home,data-overview,channel-contrib}.png`：截圖佐證

### 品質變化
| 指標 | Before | After |
|------|--------|-------|
| 部署後健康確認 | 無 | 5 頁全部 HTTP 200 |
| 效能回歸 | 未知 | 無回歸（warm 頁 -34% 至 -61%）|
| Console 錯誤 | 未知 | 無 uncaught exception（沿用 Task 05 QA 結論）|
| 截圖佐證 | Task 05 截圖 | 新增 canary 截圖更新 |

### Canary 報告摘要
- **狀態**：HEALTHY
- **Alert 數量**：0
- **首頁冷啟動**：751ms（tcp 306ms 新連線，非回歸）
- **Warm 頁均速**：29ms（比 baseline 快約 44%）
- **結論**：DEPLOY IS HEALTHY

### Cloud Canary 補充（2026-05-07）

實際對 https://pymc-marketing-mmm.streamlit.app/ 執行雲端 canary：

| 頁面 | domReady | 說明 |
|------|---------|------|
| 首頁 | 5499ms | container cold-start（免費方案 idle 重啟） |
| 資料總覽 | 536ms | TTFB 350ms 為跨洋 RTT |
| 模型擬合 | 493ms | 正常 |
| 頻道貢獻 | 471ms | 正常 |
| 預算最佳化 | 450ms | 正常 |

**結論**：雲端 app HEALTHY；warm 頁 ~500ms 在可接受範圍（Streamlit Cloud 無台灣 edge）；冷啟動 5s 為免費方案特性，非 bug。

## Iteration 11 — 2026-05-07（action-plan #11）

**目標**：對整輪 mmm-demo 產品化實驗（Tasks 0–10）進行工程回顧，總結工具效果與工作模式

### 使用工具
| 工具 | 來源 | 類型 | 用途 |
|------|------|------|------|
| `retro` | gstack | skill | git log 分析、session 偵測、skill usage 彙整、趨勢輸出 |

### 改動
- 新增 `docs/notes/tasks/11-retro.md`：task 文件（完成條件 + retro 摘要）
- 新增 `.context/retros/2026-05-07-1.json`：機器可讀 snapshot（.gitignore 排除）
- 更新 `.gitignore`：加入 `.context/` 排除
- 更新 `docs/notes/tools/skills-eval.md`：新增 retro 評比
- 更新 `docs/notes/workflow/action-plan.md`：Task 11 標記完成
- 更新 `docs/notes/README.md`：Task 11 標記完成

### 品質變化
| 指標 | Before | After |
|------|--------|-------|
| 整輪工具效果總結 | 無 | 有（11 個 skill 全部有評比記錄） |
| 工作模式可視化 | 無 | 8 sessions、commit type 分布、hotspot |
| 下輪改善點 | 無 | 3 個具體行動（gstack snooze、cloud baseline、E2E fixture） |

### 心得
- retro skill 的 session 偵測（45 分鐘 gap）精準：8 個 session 對應實際工作節奏
- raw LOC（681k）因 repo import 嚴重失真，需人工判斷；實際開發 LOC ~3,100
- `.context/retros/` JSON 人類不可讀，需要同步建 task 文件才算「完成」；retro skill 本身不會自動建 task 文件，這是流程缺口
- 首次 retro 沒有 prior history 可比較；下輪再跑才能看趨勢 delta

---

### 心得
- canary `--quick` 適合每次 push 後的 1 分鐘快速確認，不需等 10 分鐘 continuous monitor
- 冷啟動（首次 TCP 連線）vs 暖連線差距很大（751ms vs 41ms），baseline 應分別記錄
- localhost 數據與雲端差距約 10x（TTFB 差異），baseline 應分 local/cloud 兩份才有意義
- `$B console --errors` 不存在，需改用 `$B eval` 或接受 QA 階段的結論
- Streamlit Community Cloud 免費方案 container idle 後冷啟動需 5s，這是平台限制非程式問題
