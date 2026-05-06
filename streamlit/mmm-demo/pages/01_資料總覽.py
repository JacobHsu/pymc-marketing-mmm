"""頁面 1：資料總覽 — 視覺化原始資料的時間序列和分布。"""

import sys
import os

# 把 streamlit_demo/ 根目錄加到 path，讓 components 可以被 import
_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if _root not in sys.path:
    sys.path.insert(0, _root)

import streamlit as st
import pandas as pd

from components.matplotlib_config import configure_matplotlib_fonts
from components.mmm_runner import DATASETS, load_sample_data
from components.progress import render_sidebar_progress
from components.ui_helpers import icon_title
from components.charts import plot_channel_overview, plot_spend_distribution, plot_spend_share_pie

configure_matplotlib_fonts()

st.set_page_config(page_title="資料總覽", page_icon="📈", layout="wide")
render_sidebar_progress()

icon_title("table_chart", "資料總覽")
st.markdown("了解你的資料結構：銷售趨勢、各頻道花費節奏和分布。")

# ── 確保有資料（若沒有則自動載入範例）──────────────────────────────────────
if "data" not in st.session_state:
    dataset_name = list(DATASETS.keys())[0]
    df, meta = load_sample_data(dataset_name)
    st.session_state["data"] = df
    st.session_state["channel_columns"] = meta["channel_cols"]
    st.session_state["control_columns"] = meta["control_cols"]
    st.session_state["date_column"] = "date_week"
    st.session_state["target_column"] = "y"
    st.session_state["dataset_name"] = dataset_name
    dropped = meta.get("_dropped_channels", [])
    if dropped:
        st.info(f"自動載入範例資料：{dataset_name}。已略過全為零的頻道：{', '.join(dropped)}。")
    else:
        st.info(f"自動載入範例資料：{dataset_name}。如需使用自己的資料，請回首頁上傳。")

data = st.session_state["data"]
channel_cols = st.session_state.get("channel_columns", ["Google Search", "DV360", "Facebook", "AMS", "TV", "VOD", "OOH", "Radio"])
date_col = st.session_state.get("date_column", "date_week")
target_col = st.session_state.get("target_column", "y")

# ── 基本統計 ────────────────────────────────────────────────────────────────
st.subheader("基本統計摘要")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("資料週數", len(data))
with col2:
    try:
        date_min = pd.to_datetime(data[date_col]).min().strftime("%Y-%m-%d")
        date_max = pd.to_datetime(data[date_col]).max().strftime("%Y-%m-%d")
        st.metric("時間範圍", f"{date_min} ~ {date_max}")
    except Exception:
        st.metric("時間範圍", f"{data[date_col].min()} ~ {data[date_col].max()}")
with col3:
    st.metric("銷售均值", f"{data[target_col].mean():,.0f}")
with col4:
    st.metric("銷售標準差", f"{data[target_col].std():,.0f}")

with st.expander("查看原始資料前 10 列"):
    st.dataframe(data.head(10), use_container_width=True)

with st.expander("描述性統計"):
    st.dataframe(data[channel_cols + [target_col]].describe().round(4), use_container_width=True)

st.divider()

# ── 時間序列圖 ─────────────────────────────────────────────────────────────
st.subheader("時間序列：銷售額 + 各頻道花費")

with st.expander("怎麼看這張圖？", expanded=False):
    st.markdown("""
- **黑線（銷售額）**：觀察整體趨勢、季節性波動
- **彩色線（廣告花費）**：看廣告投放節奏是否與銷售高峰對應
- **注意**：因為有 Adstock（廣告遞延效應），廣告高峰後幾週銷售才會反應
    """)

try:
    if "fig_ts_overview" not in st.session_state:
        with st.spinner("繪製時間序列圖中..."):
            st.session_state["fig_ts_overview"] = plot_channel_overview(
                data, date_col, channel_cols, target_col
            )
    st.pyplot(st.session_state["fig_ts_overview"])
except Exception as e:
    st.error(f"時間序列圖繪製失敗：{e}")

st.divider()

# ── 花費分析 ───────────────────────────────────────────────────────────────
st.subheader("各頻道花費分析")

col_left, col_right = st.columns([1, 1])

with col_left:
    st.markdown("**花費分布（箱形圖）**")
    with st.expander("箱形圖說明"):
        st.markdown("中間橫線 = 中位數；箱子 = 25%-75% 分位數；鬍鬚 = 最大/最小值；圓點 = 離群值")
    try:
        if "fig_spend_box" not in st.session_state:
            with st.spinner("繪製箱形圖中..."):
                st.session_state["fig_spend_box"] = plot_spend_distribution(data, channel_cols)
        st.pyplot(st.session_state["fig_spend_box"])
    except Exception as e:
        st.error(f"箱形圖失敗：{e}")

with col_right:
    st.markdown("**花費佔比（圓餅圖）**")
    with st.expander("花費佔比的意義"):
        st.markdown("花費佔比高的頻道，在設定先驗分佈時會給較大的 sigma（允許更強的效果）")
    try:
        if "fig_spend_pie" not in st.session_state:
            with st.spinner("繪製圓餅圖中..."):
                st.session_state["fig_spend_pie"] = plot_spend_share_pie(data, channel_cols)
        st.pyplot(st.session_state["fig_spend_pie"])
    except Exception as e:
        st.error(f"圓餅圖失敗：{e}")

# 花費統計表
st.markdown("**各頻道花費統計**")
total_spend = data[channel_cols].sum().sum()
spend_summary = pd.DataFrame({
    "頻道": channel_cols,
    "總花費（標準化）": [round(data[ch].sum(), 4) for ch in channel_cols],
    "均值": [round(data[ch].mean(), 4) for ch in channel_cols],
    "最大值": [round(data[ch].max(), 4) for ch in channel_cols],
    "花費佔比 (%)": [round(data[ch].sum() / total_spend * 100, 1) for ch in channel_cols],
})
st.dataframe(spend_summary, use_container_width=True, hide_index=True)

st.divider()
st.success("資料確認完成！")
st.page_link("pages/02_模型擬合.py", label="前往「模型擬合」訓練 MMM 模型 →", icon=":material/model_training:")
