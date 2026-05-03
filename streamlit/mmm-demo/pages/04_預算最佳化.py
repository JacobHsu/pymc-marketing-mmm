"""頁面 4：預算最佳化 — 用 BudgetOptimizer 找出最佳廣告預算配置。"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from components.matplotlib_config import configure_matplotlib_fonts
from pymc_marketing.mmm.multidimensional import MultiDimensionalBudgetOptimizerWrapper

configure_matplotlib_fonts()

st.set_page_config(page_title="預算最佳化", page_icon="💰", layout="wide")

st.title("💰 預算最佳化")
st.markdown("輸入你的總廣告預算，模型會幫你找出讓銷售最大化的頻道分配方案。")

if "mmm" not in st.session_state:
    st.warning("⬅️ 請先到「模型擬合」頁面訓練模型。")
    st.stop()

mmm = st.session_state["mmm"]
data = st.session_state["data"]
channel_cols = st.session_state.get("channel_columns", ["x1", "x2"])

# ── 說明 ───────────────────────────────────────────────────────────────────
with st.expander("💡 預算最佳化是怎麼運作的？", expanded=True):
    st.markdown("""
**核心概念**：透過模型學到的飽和曲線（Response Curve），找到讓銷售最大化的預算分配。

**流程**：
1. 每個頻道都有自己的「回報曲線」（花越多，增量回報越小）
2. 最佳化算法在固定總預算下，找到讓所有頻道「邊際回報相等」的分配
3. 這個分配就是最大化總銷售的解

**注意**：最佳化結果含有不確定性（貝葉斯後驗），結果是分佈而非單點。
    """)

st.divider()

# ── 預算設定 ────────────────────────────────────────────────────────────────
st.subheader("設定總預算")

current_total = float(data[channel_cols].sum().sum())
current_by_channel = {ch: float(data[ch].sum()) for ch in channel_cols}

col1, col2 = st.columns(2)
with col1:
    budget_multiplier = st.slider(
        "預算倍數（相對現有總花費）",
        min_value=0.5,
        max_value=2.0,
        value=1.0,
        step=0.1,
        help="1.0 = 維持現有總預算，1.2 = 增加 20%，0.8 = 削減 20%"
    )
    total_budget = current_total * budget_multiplier

with col2:
    st.metric("現有總花費（標準化）", f"{current_total:.3f}")
    st.metric("目標總預算（標準化）", f"{total_budget:.3f}")
    if budget_multiplier > 1.0:
        st.caption(f"📈 增加 {(budget_multiplier - 1) * 100:.0f}% 預算")
    elif budget_multiplier < 1.0:
        st.caption(f"📉 削減 {(1 - budget_multiplier) * 100:.0f}% 預算")
    else:
        st.caption("➡️ 維持現有總預算")

st.divider()

# ── 執行最佳化 ─────────────────────────────────────────────────────────────
st.subheader("執行最佳化")

optimize_btn = st.button("🔍 計算最佳預算配置", type="primary", use_container_width=True)

if optimize_btn:
    with st.spinner("正在計算最佳配置..."):
        try:
            last_date = pd.to_datetime(data["date_week"]).max()
            num_periods = len(data)

            wrapper = MultiDimensionalBudgetOptimizerWrapper(
                model=mmm,
                start_date=last_date + pd.Timedelta(weeks=1),
                end_date=last_date + pd.Timedelta(weeks=num_periods),
            )

            optimal, res = wrapper.optimize_budget(
                budget=total_budget,
                response_variable="total_media_contribution_original_scale",
            )

            # optimal 是 xr.DataArray，轉成 {channel: total_budget} dict
            allocation = {
                str(ch): float(optimal.sel(channel=ch).sum())
                for ch in optimal.coords["channel"].values
            }

            st.session_state["budget_result"] = {"simulated": False, "allocation": allocation}
            st.session_state["budget_total"] = total_budget
            st.success("✅ 最佳化完成！")

        except Exception as e:
            st.error(f"最佳化失敗：{e}")
            st.stop()

# ── 顯示結果 ────────────────────────────────────────────────────────────────
if "budget_result" in st.session_state:
    result = st.session_state["budget_result"]
    budget_total = st.session_state["budget_total"]

    st.divider()
    st.subheader("最佳配置結果")

    is_simulated = result.get("simulated", False)
    if is_simulated:
        st.info("ℹ️ 以下為**教學示意**結果（模擬），實際結果需要完整資料和更多採樣次數。")
    allocation = result["allocation"]

    # 比較現有 vs 最佳配置
    comparison_data = []
    for ch in channel_cols:
        current = current_by_channel[ch]
        optimal = allocation.get(ch, current)
        change = optimal - current
        change_pct = (change / current * 100) if current > 0 else 0
        comparison_data.append({
            "頻道": ch,
            "現有花費": round(current, 4),
            "最佳花費": round(optimal, 4),
            "增減量": round(change, 4),
            "增減 (%)": round(change_pct, 1),
        })

    comparison_df = pd.DataFrame(comparison_data)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**花費配置比較表**")
        def color_change(val: float) -> str:
            if val > 0:
                return "color: green"
            elif val < 0:
                return "color: red"
            return ""

        st.dataframe(
            comparison_df.style.map(color_change, subset=["增減量", "增減 (%)"]),
            use_container_width=True,
            hide_index=True,
        )

    with col2:
        st.markdown("**現有 vs 最佳配置（長條圖）**")
        fig, ax = plt.subplots(figsize=(6, 4))
        x = np.arange(len(channel_cols))
        width = 0.35
        current_vals = [current_by_channel[ch] for ch in channel_cols]
        optimal_vals = [allocation.get(ch, current_by_channel[ch]) for ch in channel_cols]

        bars1 = ax.bar(x - width / 2, current_vals, width, label="現有配置", color="gray", alpha=0.7)
        bars2 = ax.bar(x + width / 2, optimal_vals, width, label="最佳配置", color="C0", alpha=0.8)

        ax.bar_label(bars1, labels=[f"{v:.3f}" for v in current_vals], padding=3, fontsize=9)
        ax.bar_label(bars2, labels=[f"{v:.3f}" for v in optimal_vals], padding=3, fontsize=9)

        ax.set_xticks(x)
        ax.set_xticklabels(channel_cols)
        ax.set(title="預算配置比較", ylabel="花費（標準化）")
        ax.legend()
        fig.tight_layout()
        st.pyplot(fig)

    st.divider()

    # 建議摘要
    st.subheader("📋 配置建議摘要")
    for _, row in comparison_df.iterrows():
        change_pct = row["增減 (%)"]
        if change_pct > 5:
            emoji = "📈"
            advice = f"建議**增加**投入，ROAS 較高"
        elif change_pct < -5:
            emoji = "📉"
            advice = f"建議**削減**投入，資金轉移到效益更高的頻道"
        else:
            emoji = "➡️"
            advice = f"接近最佳配置，**維持現狀**即可"

        st.markdown(f"{emoji} **頻道 {row['頻道']}**：{advice}（建議調整 {change_pct:+.1f}%）")

st.divider()
st.markdown("---")
st.markdown("**🎓 學習重點**：預算最佳化是 MMM 最有商業價值的應用，它把統計模型轉化為可執行的行動建議。")
