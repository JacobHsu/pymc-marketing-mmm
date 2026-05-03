"""MMM 互動 DEMO 主頁 — 繁體中文介面。

啟動方式：
    conda activate pymc-marketing-dev
    cd sandbox/streamlit_demo
    streamlit run app.py
"""

import streamlit as st
import sys
import os
from dotenv import load_dotenv

# 載入 .env（NVIDIA_API_KEY 等），須在所有 st.* 呼叫之前執行
load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

# 確保 components 可以被匯入
sys.path.insert(0, os.path.dirname(__file__))

from components.mmm_runner import load_sample_data

st.set_page_config(
    page_title="MMM 行銷組合模型 DEMO",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── 側邊欄：資料載入 ──────────────────────────────────────────────────────
st.sidebar.title("📊 MMM DEMO")
st.sidebar.markdown("**行銷組合模型互動展示**")
st.sidebar.divider()

data_source = st.sidebar.radio(
    "選擇資料來源",
    ["使用範例資料", "上傳自己的 CSV"],
    index=0,
)

if data_source == "使用範例資料":
    if "data" not in st.session_state:
        df, meta = load_sample_data()
        st.session_state["data"] = df
        st.session_state["channel_columns"] = meta["channel_cols"]
        st.session_state["control_columns"] = meta["control_cols"]
        st.session_state["date_column"] = "date_week"
        st.session_state["target_column"] = "y"
    st.sidebar.success("✓ 已載入範例資料（mock_cgp）")
else:
    uploaded = st.sidebar.file_uploader("上傳 CSV 檔案", type=["csv"])
    if uploaded:
        data = pd.read_csv(uploaded, parse_dates=True)
        st.session_state["data"] = data
        st.sidebar.success(f"✓ 已載入：{uploaded.name}（{len(data)} 列）")

        # 讓使用者選擇欄位
        cols = data.columns.tolist()
        st.sidebar.subheader("欄位設定")
        date_col = st.sidebar.selectbox("日期欄位", cols)
        target_col = st.sidebar.selectbox("目標變數（銷售額）", cols)
        channel_cols = st.sidebar.multiselect("媒體頻道欄位", [c for c in cols if c not in [date_col, target_col]])
        control_cols = st.sidebar.multiselect("控制變數欄位", [c for c in cols if c not in [date_col, target_col] + channel_cols])

        st.session_state["channel_columns"] = channel_cols
        st.session_state["control_columns"] = control_cols
        st.session_state["date_column"] = date_col
        st.session_state["target_column"] = target_col

st.sidebar.divider()
st.sidebar.caption("💡 先在「資料總覽」頁面檢視資料，再到「模型擬合」頁面訓練模型。")

# ── 主頁內容 ──────────────────────────────────────────────────────────────
st.title("📊 MMM 行銷組合模型 互動 DEMO")
st.markdown("> **目標**：用真實資料學習 Media Mix Modeling，理解各廣告頻道對銷售的貢獻。")

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🎯 什麼是 MMM？")
    st.markdown("""
**Media Mix Modeling（行銷組合模型）** 是一種統計方法，幫助行銷人員回答：

- 哪個廣告頻道帶來最多銷售？
- 每個頻道的 ROAS 是多少？
- 如何重新分配預算才能最大化 ROI？

PyMC-Marketing 使用**貝葉斯統計**建立 MMM，
不只給點估計，還量化**不確定性**。
    """)

with col2:
    st.markdown("### ⚙️ 核心概念")
    st.markdown("""
**Adstock（廣告遞延效應）**
廣告效果不會立刻消失，會延續到未來幾週後才慢慢遞減。

**Saturation（飽和效應）**
廣告花費越多，邊際效益越低：
- 第一塊錢效果最大
- 之後每塊錢效果遞減

**貝葉斯推論**
不是只給一個答案，而是給一個「可能性分佈」，
量化我們對結果的不確定性。
    """)

with col3:
    st.markdown("### 🗺️ 使用流程")
    st.markdown("""
1. **資料總覽** → 了解資料結構和統計
2. **模型擬合** → 訓練 MMM（需要幾分鐘）
3. **頻道貢獻** → 分析各頻道效果和 ROAS
4. **預算最佳化** → 找到最佳預算配置
    """)

st.divider()

if "data" in st.session_state:
    data = st.session_state["data"]
    st.success(f"✓ 資料已載入：{len(data)} 週的資料，{len(data.columns)} 個欄位")

    metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)
    target_col = st.session_state.get("target_column", "y")
    channel_cols = st.session_state.get("channel_columns", [])

    with metric_col1:
        st.metric("資料筆數", f"{len(data)} 週")
    with metric_col2:
        st.metric("廣告頻道數", len(channel_cols))
    with metric_col3:
        if target_col in data.columns:
            st.metric("平均銷售額", f"{data[target_col].mean():,.0f}")
    with metric_col4:
        if channel_cols:
            total_spend = data[channel_cols].sum().sum()
            st.metric("總廣告花費（標準化）", f"{total_spend:.1f}")

    st.info("👈 點擊左側導覽列，前往各功能頁面。建議從「資料總覽」開始。")
else:
    st.warning("⬅️ 請先在左側選擇資料來源。")
