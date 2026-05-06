# MMM Streamlit Demo

以互動網頁展示完整 Media Mix Modeling（MMM）工作流程：載入行銷資料 → 擬合模型 → 分析通路 ROAS → 預算最佳化。

線上版本（部署後）：待補

---

## 快速啟動

> 環境已建好的情況下，一行指令啟動：

```powershell
.\streamlit\mmm-demo\run.ps1
```

或在 `streamlit/mmm-demo/` 目錄下直接執行：

```powershell
.\run.ps1
```

瀏覽器自動開啟 `http://localhost:8501`。停止服務按 `Ctrl + C`。

瀏覽器自動開啟 `http://localhost:8501`。停止服務按 `Ctrl + C`。

---

## 第一次環境建置（Windows + conda）

### 1. 建立 conda 環境

```powershell
conda create -n pymc-marketing-dev -c conda-forge --override-channels python=3.12 pip -y
conda activate pymc-marketing-dev
```

### 2. 安裝專案與依賴

```powershell
pip install -e .
pip install streamlit matplotlib pandas openai python-dotenv huggingface_hub
```

### 3. 安裝 C++ 編譯器（強烈建議）

```powershell
conda install -c conda-forge gxx -y
```

未安裝時 PyMC 採樣速度慢 3–5 倍（`draws=100` 約需 5–15 分鐘而非 30–60 秒）。

### 4. 啟動

```powershell
cd streamlit\mmm-demo
streamlit run app.py
```

---

## 頁面說明

| 頁面 | 功能 |
|------|------|
| 資料總覽 | 查看時間趨勢、通路花費分布 |
| 模型擬合 | 設定參數、執行 MCMC 採樣 |
| 頻道貢獻 | 通路貢獻、ROAS、AI 行銷洞察 |
| 預算最佳化 | 模擬預算調整方案 |

新手測試時建議調小採樣參數：`draws=200`、`chains=1`。

---

## AI 行銷洞察（選用，免費）

使用 NVIDIA NIM 免費 API，由 `meta/llama-3.3-70b-instruct` 分析 ROAS 數據並給出繁體中文預算建議。

**取得 API Key：** [build.nvidia.com](https://build.nvidia.com) → 右上角 API Keys → 建立（格式 `nvapi-...`）

**使用：** 進入「頻道貢獻」頁面 → 展開「🤖 AI 行銷洞察」→ 貼上 Key → 開始分析

**免每次輸入，用 `.env` 設定：**

```powershell
cp .env.sample .env
# 編輯 .env，填入 NVIDIA_API_KEY=nvapi-...
```

---

## 目錄結構

```text
streamlit/mmm-demo/
├── app.py                   # 主入口
├── requirements.txt         # 雲端部署依賴
├── .env.sample              # 環境變數範本
├── pages/
│   ├── 01_資料總覽.py
│   ├── 02_模型擬合.py
│   ├── 03_頻道貢獻.py
│   └── 04_預算最佳化.py
├── components/
│   ├── mmm_runner.py        # MMM 建模（含 HF Hub 自動下載模型）
│   ├── ai_analysis.py       # AI 行銷洞察
│   ├── charts.py            # 圖表
│   └── matplotlib_config.py # 中文字型設定
└── data/
    ├── mock_cgp_data.csv    # 預設資料（8 頻道）
    └── fitted_mmm.nc        # 已擬合模型（本機用，不進 git）
```

---

## 常見問題

**`ModuleNotFoundError: No module named 'pymc_extras'`**
→ 忘記 activate 環境，或未安裝專案。執行：
```powershell
conda activate pymc-marketing-dev
pip install -e .
```

**`WARNING: g++ not available`**
→ 未裝 C++ 編譯器，採樣變慢。執行：
```powershell
conda install -c conda-forge gxx -y
```

**圖表中文顯示方框**
→ 重啟 Streamlit（`Ctrl+C` 後再 `streamlit run app.py`）。

**`localhost:8501` 打不開**
→ 確認 PowerShell 裡服務還在跑。若 port 被占用：
```powershell
streamlit run app.py --server.port 8502
```

**AI 分析失敗：`AuthenticationError`**
→ API Key 格式需為 `nvapi-...`，至 [build.nvidia.com](https://build.nvidia.com) 確認 Key 有效。

---

## 雲端部署（Streamlit Community Cloud）

> 與 mmm-explainer 相同平台，免費、無需伺服器。

### 前置條件

| 必要 | 說明 |
|------|------|
| GitHub repo | 程式碼需推送至 GitHub public/private repo |
| Streamlit Community Cloud 帳號 | [share.streamlit.io](https://share.streamlit.io) 免費方案 |
| Hugging Face 帳號（可選） | 存放 `fitted_mmm.nc`，若不需 AI 模型預載可跳過 |

---

### Step 1：上傳模型檔到 Hugging Face（若需要預載模型）

Streamlit Cloud 是無狀態容器，`data/fitted_mmm.nc` **不能放進 git**（檔案太大），需改從 HF Hub 下載。

```bash
# 安裝 HF CLI
pip install huggingface_hub

# 登入（只需做一次）
huggingface-cli login

# 建立 dataset repo（若尚未建立）
# 至 https://huggingface.co/new-dataset 建立，例如 jacobhsutw/mmm-demo-model

# 上傳模型檔
huggingface-cli upload jacobhsutw/mmm-demo-model data/fitted_mmm.nc fitted_mmm.nc --repo-type dataset
```

---

### Step 2：確認 .gitignore 排除本機敏感檔

```gitignore
streamlit/mmm-demo/.env
streamlit/mmm-demo/data/fitted_mmm.nc
streamlit/mmm-demo/data/fitted_mmm.nc.bak
```

---

### Step 3：推送至 GitHub

```powershell
git add streamlit/mmm-demo/
git commit -m "feat: add mmm-demo streamlit app"
git push origin main
```

---

### Step 4：在 Streamlit Community Cloud 建立 App

1. 前往 [share.streamlit.io](https://share.streamlit.io) → **Create app**
2. 填入：
   | 欄位 | 值 |
   |------|-----|
   | Repository | `JacobHsu/pymc-marketing-mmm` |
   | Branch | `main` |
   | Main file path | `streamlit/mmm-demo/app.py` |
3. 點 **Advanced settings**，設定以下兩項後點 **Deploy**

---

### Step 5：Advanced settings 設定

**Python version** → 選 `3.12`

**Secrets** → 填入以下內容（TOML 格式，字串值必須加雙引號）：

```toml
NVIDIA_API_KEY = "nvapi-your-key-here"
HF_REPO_ID = "jacobhsutw/mmm-demo-model"
```

> **注意**：格式與本機 `.env` 不同。`.env` 用 `KEY=value`，Streamlit Secrets 用 `KEY = "value"`（等號兩側空格，值加雙引號）。

> Streamlit Cloud 的 Secrets 等同本機的 `.env`，不會暴露在 GitHub。

---

### Step 6：等待部署完成

首次部署需安裝 PyMC 等重套件，約需 **5–10 分鐘**。部署完成後網址格式：
`https://your-app-name.streamlit.app/`

---

### 常見部署問題

**`Invalid format: please enter valid TOML`**
→ Secrets 格式錯誤。確認每個值都加了雙引號，例如 `KEY = "value"`，不能寫成 `KEY=value`。

**`ModuleNotFoundError` on Streamlit Cloud**
→ 確認 `requirements.txt` 包含所有依賴，且路徑為 `streamlit/mmm-demo/requirements.txt`。

**模型檔找不到**
→ 確認 `HF_REPO_ID` Secret 已設定，且 HF dataset repo 為 **Public**（或提供 HF Token）。

**部署超時（Timeout）**
→ PyMC 初始化較慢屬正常。若持續逾時可在 App Settings 增加 Memory。

---

## 相關資料

- [PyMC-Marketing 專案 README](../../README.zh-TW.md)
- [MMM quickstart notebook](../../docs/source/notebooks/mmm/mmm_quickstart.ipynb)
- [官方 mmm-explainer App](../mmm-explainer/README.zh-TW.md)
