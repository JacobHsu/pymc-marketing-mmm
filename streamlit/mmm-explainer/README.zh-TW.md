# MMM 視覺化互動 App（Streamlit）

## 簡介

這個 Streamlit App 以互動圖表呈現行銷組合模型（MMM）的核心概念，包括：
- **Adstock（廣告存留效果）**
- **Saturation（飽和曲線）**
- **Bayesian Priors（貝葉斯先驗分佈）**
- **Fourier Modes（季節性傅立葉項）**
- **Time-Varying Parameters（時變參數）**

線上版本：https://pymc-marketing-app.streamlit.app/

---

## 本地啟動

### 1. 建立環境

```bash
conda activate pymc-marketing-dev
```

### 2. 安裝額外依賴

```bash
pip install -r streamlit/mmm-explainer/requirements.txt
```

> 主要套件：`streamlit==1.46.1`、`plotly==6.3.0`、`preliz==0.20.0`

### 3. 啟動 App

```bash
cd streamlit/mmm-explainer
streamlit run Visualise_Priors.py
```

瀏覽器會自動開啟 `http://localhost:8501`

---

## 功能說明

### Adstock 轉換
廣告投放後的延遲效果。調整衰減率（decay rate）和最大延遲期數（l_max），觀察廣告效果如何隨時間遞減。

### Saturation 飽和曲線
行銷花費的邊際遞減效應。支援多種飽和函數：
- Logistic（邏輯斯迪克）
- Tanh（雙曲正切）
- Michaelis-Menten

### Bayesian Priors 先驗分佈
互動調整各種機率分佈的參數，理解 Bayesian MMM 如何用先驗知識約束模型。支援 Normal、HalfNormal、Beta 等十多種分佈。

### Fourier Modes 季節性
用傅立葉項捕捉週期性趨勢（週、月、年）。調整週期和模式數量，觀察季節效果的形狀。

### Time-Varying Parameters 時變參數
媒體效果隨時間變化的建模方式。

---

## 與 `sandbox/streamlit_demo` 的差異

| | mmm-explainer | streamlit_demo |
|---|---|---|
| 用途 | 教學：理解 MMM 參數 | 實戰：載入資料、跑模型、看 ROAS |
| 需要模型檔 | 不需要 | 需要 `fitted_mmm.nc` |
| AI 分析 | 無 | 有（NVIDIA NIM） |
| 部署狀態 | 已上線 | 開發中 |
