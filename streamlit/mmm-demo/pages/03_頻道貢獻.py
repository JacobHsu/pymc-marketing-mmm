"""頁面 3：頻道貢獻 — 分析各廣告頻道的效果和 ROAS。"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import streamlit as st
import matplotlib.pyplot as plt

from components.matplotlib_config import configure_matplotlib_fonts
from components.mmm_runner import get_channel_roas
from components.charts import (
    plot_channel_contribution_over_time,
    plot_roas_bar,
    plot_waterfall,
)
from components.ai_analysis import analyze_roas_with_llm
from components.progress import render_sidebar_progress

configure_matplotlib_fonts()

st.set_page_config(page_title="頻道貢獻", page_icon="📊", layout="wide")
render_sidebar_progress()

st.title("📊 頻道貢獻分析")
st.markdown("了解各廣告頻道對銷售的貢獻，以及廣告花費回報率（ROAS）。")

if "mmm" not in st.session_state:
    st.warning("⬅️ 請先到「模型擬合」頁面訓練模型。")
    st.page_link("pages/02_模型擬合.py", label="前往模型擬合", icon="⚙️")
    st.stop()

mmm = st.session_state["mmm"]
data = st.session_state["data"]
channel_cols = st.session_state.get("channel_columns", ["x1", "x2"])

# ── ROAS 摘要 ─────────────────────────────────────────────────────────────
st.subheader("各頻道 ROAS 摘要")

with st.expander("💡 ROAS 是什麼？"):
    st.markdown("""
**ROAS = Return on Ad Spend（廣告花費回報率）**

計算公式：**ROAS = 廣告帶來的銷售額 / 廣告花費**

- ROAS = 3.0 → 花 1 元廣告，帶來 3 元銷售
- ROAS > 1 → 廣告有正向回報
- ROAS < 1 → 廣告虧損（需重新評估）

**注意**：這裡的 ROAS 是「模型估計的 ROAS」，含有不確定性（貝葉斯後驗）。
    """)

if "roas_df" not in st.session_state:
    with st.spinner("計算各頻道 ROAS..."):
        st.session_state["roas_df"] = get_channel_roas(mmm, data)
roas_df = st.session_state["roas_df"]

metric_cols = st.columns(len(channel_cols))
for i, (_, row) in enumerate(roas_df.iterrows()):
    with metric_cols[i]:
        st.metric(
            label=f"頻道 {row['頻道']} ROAS",
            value=f"{row['ROAS']:.2f}x",
            delta=f"貢獻 {row['總貢獻（銷售額）']:,.0f}",
        )

st.divider()

# ── ROAS 比較圖 ────────────────────────────────────────────────────────────
st.subheader("ROAS 比較")
col1, col2 = st.columns([2, 1])
with col1:
    if "fig_roas" not in st.session_state:
        with st.spinner("繪製 ROAS 圖..."):
            st.session_state["fig_roas"] = plot_roas_bar(roas_df)
    st.pyplot(st.session_state["fig_roas"])
with col2:
    st.markdown("**各頻道詳細數據**")
    display_df = roas_df.copy()
    display_df["總貢獻（銷售額）"] = display_df["總貢獻（銷售額）"].round(0).astype(int)
    display_df["總花費"] = display_df["總花費"].round(4)
    display_df["ROAS"] = display_df["ROAS"].round(3)
    st.dataframe(display_df, use_container_width=True, hide_index=True)

st.divider()

# ── 貢獻時間序列 ───────────────────────────────────────────────────────────
st.subheader("各頻道銷售貢獻（時間序列）")
with st.expander("💡 怎麼看這張圖？"):
    st.markdown("""
- 彩色填滿區域 = 各頻道在每週的銷售貢獻量
- 貢獻越高的頻道，填滿面積越大
- 觀察貢獻是否和廣告花費節奏一致（考慮 Adstock 延遲）
    """)

if "fig_contrib_time" not in st.session_state:
    with st.spinner("繪製貢獻時間序列..."):
        st.session_state["fig_contrib_time"] = plot_channel_contribution_over_time(mmm)
st.pyplot(st.session_state["fig_contrib_time"])

# ── AI ROAS 分析 ───────────────────────────────────────────────────────────
with st.expander("🤖 AI 行銷洞察", expanded=False):
    st.markdown("AI 直接讀取 ROAS 數據，給出預算分配建議。不需要圖片辨識，分析更精準。")

    _env_key = os.environ.get("NVIDIA_API_KEY", "")
    if _env_key:
        st.caption("✓ API Key 已從環境變數載入")
        nvidia_key = _env_key
    else:
        nvidia_key = st.text_input(
            "NVIDIA API Key",
            type="password",
            placeholder="nvapi-...",
            help="從 https://build.nvidia.com → API Keys 取得免費金鑰。",
        )

    if st.button("🔍 開始 AI 分析", type="primary"):
        if not nvidia_key.strip():
            st.error("請輸入 NVIDIA API Key。")
        else:
            with st.spinner("AI 分析中，請稍候..."):
                try:
                    analysis = analyze_roas_with_llm(
                        roas_df=roas_df,
                        api_key=nvidia_key.strip(),
                    )
                    st.session_state["chart_analysis"] = analysis
                except Exception as e:
                    st.error(f"AI 分析失敗：{e}")

    if "chart_analysis" in st.session_state:
        st.markdown("**📋 AI 分析結果**")
        st.markdown(st.session_state["chart_analysis"])

st.divider()

# ── 瀑布圖 ─────────────────────────────────────────────────────────────────
st.subheader("銷售貢獻瀑布圖（整體分解）")
with st.expander("💡 瀑布圖說明"):
    st.markdown("""
這張圖回答：**「過去這段時間，總銷售額是怎麼組成的？」**

- **基線（Intercept）**：不受廣告影響的自然銷售
- **廣告頻道（Channels）**：各頻道的廣告貢獻總和
- **控制變數（Controls）**：促銷、假日等事件的影響
- **季節性（Seasonality）**：年度週期性的影響
    """)

try:
    if "fig_waterfall" not in st.session_state:
        with st.spinner("繪製瀑布圖..."):
            st.session_state["fig_waterfall"] = plot_waterfall(mmm)
    st.pyplot(st.session_state["fig_waterfall"])
except Exception as e:
    st.warning(f"瀑布圖暫時無法顯示：{e}")

st.divider()

# ── 頻道貢獻佔比 ──────────────────────────────────────────────────────────
st.subheader("各頻道貢獻佔比")
try:
    if "fig_contrib_share" not in st.session_state:
        with st.spinner("繪製貢獻佔比圖..."):
            result_share = mmm.plot.channel_contribution_share_hdi(figsize=(10, 4))
            st.session_state["fig_contrib_share"] = (
                result_share[0] if isinstance(result_share, tuple) else result_share
            )
    st.pyplot(st.session_state["fig_contrib_share"])
except Exception as e:
    st.warning(f"貢獻佔比圖暫時無法顯示：{e}")

st.divider()
st.success("✅ 分析完成！")
st.page_link("pages/04_預算最佳化.py", label="前往「預算最佳化」尋找最佳預算配置 →", icon="💰")
