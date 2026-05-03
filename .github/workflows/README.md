# GitHub Actions Workflows

## 決策原則

1. **專注目標**：Streamlit 開發與部屬
2. **控制 usage**：避免自動觸發的高耗時 workflow
3. **學習價值**：保留值得研究的 CI/CD 與 AI 自動化範例

---

## 保留的 Workflows

### 直接有用

| 檔案 | 觸發 | 說明 |
|------|------|------|
| `streamlit_url_health.yml` | 每天定時 | 檢查 Streamlit app 是否在線。原版每 6 小時一次，已改為每天一次節省 usage。部屬後填入自己的 URL |

### 值得學習：AI 自動化（cc-gha 系列）

**cc = Claude Code，gha = GitHub Actions**
在 GitHub issue 貼上對應 label，Claude 會自動在雲端執行對應工作並開 PR。
需在 repo secrets 設定 `ANTHROPIC_API_KEY`。

| 檔案 | Label | Claude 做什麼 | Timeout |
|------|-------|-------------|---------|
| `cc-gha-research.yml` | `research_needed` | 研究問題、查文件 | 30 分鐘 |
| `cc-gha-plan.yml` | `plan_needed` | 寫實作計畫 | 20 分鐘 |
| `cc-gha-implement.yml` | `implement` | 照計畫寫程式碼、開 PR | 30 分鐘 |
| `cc-gha-iterate.yml` | `iterate` | 根據 PR review 修改 | 20 分鐘 |

流程：`research_needed` → `plan_needed` → `implement` → `iterate`

### 值得學習：Issue 自動化

| 檔案 | 觸發 | 說明 |
|------|------|------|
| `triage.yml` | issue opened | AI 自動分類 issue |
| `duplicate-issues.yml` | issue opened / edited | AI 偵測重複 issue |

### 值得學習：PR 自動化

| 檔案 | 觸發 | 說明 |
|------|------|------|
| `pr-auto-label.yml` | PR opened | 依變動檔案自動貼 label |

---

## 移除的 Workflows

### 因 usage 移除

| 檔案 | 原觸發 | usage 影響 | 移除原因 |
|------|--------|-----------|---------|
| `test.yml` | push / PR to main | **每次 168 分鐘**（24 jobs 並行） | 每次 push 自動燒，個人專案不需要 |
| `pypi.yml` | push / PR to main | 每次數分鐘 | 不發佈 PyPI |

### 因與本專案無關移除

| 檔案 | 說明 |
|------|------|
| `test_notebook.yml` | 跑 Jupyter notebook 測試，不維護 notebook |
| `generate-test-durations.yml` | 配合 test.yml 的測試分組計時，test.yml 移除後無意義 |
| `broken-link-checker.yml` | 檢查官方文件站連結，無對外文件站 |
| `install-conda-env.yml` | 測試 conda 環境安裝流程 |
| `uml.yml` | 自動產生套件 UML 架構圖 |
| `bot-prs.yml` | 幫 bot 開的 PR 自動貼 label |
| `rtd-link-preview.yml` | ReadTheDocs 文件預覽，未使用該平台 |
