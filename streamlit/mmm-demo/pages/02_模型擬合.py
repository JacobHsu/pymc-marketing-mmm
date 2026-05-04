"""頁面 2：模型擬合 — 設定參數並執行 MMM 訓練。"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import streamlit as st

from components.mmm_runner import (
    build_mmm, fit_mmm, sample_posterior_predictive,
    save_mmm, load_mmm, saved_model_exists,
)
from components.charts import plot_posterior_predictive
from components.ai_analysis import analyze_fit_with_llm
from components.progress import render_sidebar_progress

st.set_page_config(page_title="模型擬合", page_icon="⚙️", layout="wide")
render_sidebar_progress()

st.title("⚙️ 模型擬合")

with st.expander("💡 為什麼要做模型擬合？", expanded=True):
    st.markdown("""
這份資料模擬一家消費品公司（CPG）同時在 8 個媒體頻道投放廣告的情境。

**模型擬合要回答的問題：**

| 問題 | 說明 |
|------|------|
| 哪個頻道真正帶來銷售？ | TV 花最多，但效果不一定最好 |
| 廣告效果多久後才反應？ | 這週投電視廣告，幾週後才看到銷售成長（Adstock 遞延效應） |
| 每花 1 元帶回多少銷售？ | ROAS（Return on Ad Spend），在「頻道貢獻」頁查看 |
| 預算怎麼分配最有效？ | 在「預算最佳化」頁模擬調整 |

MMM 用 **MCMC 採樣**估計以上問題的答案，並給出不確定性範圍（不只是點估計）。
    """)

st.markdown(
    "預設參數為**快速 Demo 模式**，適合初次體驗流程。"
    "  \n⚠️ 若終端機出現 `g++ not available`，採樣速度會慢 3–5 倍（約 5–15 分鐘）。"
    "  \n建議先執行 `conda install -c conda-forge gxx -y` 安裝編譯器後再跑。"
)

if "data" not in st.session_state:
    st.warning("⬅️ 請先回到首頁載入資料。")
    st.stop()

data = st.session_state["data"]
channel_cols = st.session_state.get("channel_columns", ["Google Search", "DV360", "Facebook", "AMS", "TV", "VOD", "OOH", "Radio"])
control_cols = st.session_state.get("control_columns", ["Numeric Distribution", "RSP", "Promotion"])

# ── 載入存檔 ────────────────────────────────────────────────────────────────
if "mmm" not in st.session_state and saved_model_exists():
    import os as _os
    from components.mmm_runner import SAVE_PATH, HF_REPO_ID
    if _os.path.exists(SAVE_PATH):
        st.info("💾 偵測到本地模型，可直接載入跳過採樣。")
    else:
        st.info(f"☁️ 將從 HuggingFace 下載模型（`{HF_REPO_ID}`），首次載入約需 10 秒。")
    if st.button("⚡ 載入上次擬合結果", type="primary", use_container_width=True):
        with st.spinner("載入模型中..." if _os.path.exists(SAVE_PATH) else "從 HuggingFace 下載模型中..."):
            try:
                mmm = load_mmm()
                st.session_state["mmm"] = mmm
                for _k in ("fit_analysis", "roas_df", "fig_roas", "fig_contrib_time", "fig_waterfall", "fig_contrib_share"):
                    st.session_state.pop(_k, None)
            except Exception as e:
                st.error(f"載入失敗：{e}")
                st.stop()
        nvidia_key = os.environ.get("NVIDIA_API_KEY", "")
        if nvidia_key:
            with st.spinner("🤖 AI 診斷中..."):
                try:
                    analysis = analyze_fit_with_llm(mmm, data, nvidia_key)
                    st.session_state["fit_analysis"] = analysis
                except Exception as e:
                    st.session_state["fit_analysis"] = f"（AI 分析失敗：{e}）"
        st.rerun()
    st.divider()

# ── 模型設定 ────────────────────────────────────────────────────────────────
st.subheader("模型設定")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Adstock 設定**")
    l_max = st.slider(
        "最大延遲週數（l_max）",
        min_value=2,
        max_value=16,
        value=4,
        help="廣告效果最多延遲幾週。設越大模型越複雜，採樣越慢。快速 Demo 用 4。"
    )
    yearly_seasonality = st.slider(
        "年度季節性項數（yearly_seasonality）",
        min_value=1,
        max_value=6,
        value=1,
        help="傅立葉項數量。越多越能捕捉季節性，但採樣越慢。快速 Demo 用 1。"
    )
    with st.expander("💡 l_max 怎麼選？"):
        st.markdown("""
- **電視廣告**：通常 8-12 週
- **數位廣告**：通常 2-4 週
- **不確定時**：從 8 開始（quickstart 的預設值）
        """)

with col2:
    st.markdown("**採樣設定（影響速度 vs 精度）**")
    draws = st.slider(
        "採樣次數（draws）",
        min_value=100,
        max_value=2000,
        value=100,
        step=100,
        help="越多越精確，但越慢。快速 Demo 用 100，正式分析用 500+。"
    )
    chains = st.select_slider(
        "鏈數（chains）",
        options=[1, 2, 4],
        value=1,
        help="多鏈用於診斷收斂。快速 Demo 用 1，正式分析用 2。"
    )
    target_accept = st.slider(
        "目標接受率（target_accept）",
        min_value=0.8,
        max_value=0.99,
        value=0.80,
        step=0.01,
        help="越高越謹慎，步長越小，採樣越慢但發散越少。快速 Demo 用 0.80。"
    )

st.divider()

# ── 執行擬合 ────────────────────────────────────────────────────────────────
st.subheader("執行模型擬合")

# 顯示當前設定摘要
with st.expander("📋 當前設定摘要"):
    st.markdown(f"""
| 參數 | 值 |
|------|-----|
| 媒體頻道 | {', '.join(channel_cols)} |
| 控制變數 | {', '.join(control_cols)} |
| 最大延遲週數 | {l_max} 週 |
| 年度季節性項數 | {yearly_seasonality} |
| 採樣次數 | {draws} |
| 鏈數 | {chains} |
| 目標接受率 | {target_accept} |
| 預計採樣次數 | {draws * chains:,} 次 |
    """)

fit_button = st.button("🚀 開始擬合模型", type="primary", use_container_width=True)

if fit_button:
    # 進度分配：建模 5%、採樣 80%、後驗預測 15%
    SAMPLE_START = 5
    SAMPLE_END = 85
    progress_bar = st.progress(0)
    status_text = st.empty()

    def on_draw(ratio: float) -> None:
        pct = int(SAMPLE_START + ratio * (SAMPLE_END - SAMPLE_START))
        progress_bar.progress(pct)
        status_text.info(
            f"⛓️ MCMC 採樣中 {int(ratio * 100)}%"
            f"（{int(ratio * draws * chains)}/{draws * chains} draws）"
            f"  ⏱ 請耐心等待，請勿關閉頁面。"
        )

    try:
        progress_bar.progress(SAMPLE_START)
        status_text.info("📐 建立模型結構中...")
        mmm = build_mmm(
            data=data,
            channel_columns=channel_cols,
            control_columns=control_cols,
            l_max=l_max,
            yearly_seasonality=yearly_seasonality,
        )

        status_text.info(f"⛓️ MCMC 採樣中 0%（0/{draws * chains} draws）  ⏱ 請耐心等待，請勿關閉頁面。")
        mmm = fit_mmm(
            mmm=mmm,
            data=data,
            draws=draws,
            chains=chains,
            target_accept=target_accept,
            on_draw=on_draw,
        )

        progress_bar.progress(SAMPLE_END)
        status_text.info("📊 計算後驗預測中...")
        mmm = sample_posterior_predictive(mmm, data)

        progress_bar.progress(100)
        status_text.empty()

        st.session_state["mmm"] = mmm
        st.session_state["fit_config"] = {
            "l_max": l_max,
            "draws": draws,
            "chains": chains,
            "target_accept": target_accept,
        }
        for _k in ("fit_analysis", "roas_df", "fig_roas", "fig_contrib_time", "fig_waterfall", "fig_contrib_share"):
            st.session_state.pop(_k, None)

        with st.spinner("💾 存檔中..."):
            try:
                save_path = save_mmm(mmm)
                st.success(f"✅ 模型擬合完成，已自動存檔。")
            except Exception as e:
                st.success("✅ 模型擬合完成！")
                st.warning(f"存檔失敗（不影響本次使用）：{e}")

        nvidia_key = os.environ.get("NVIDIA_API_KEY", "")
        if nvidia_key:
            with st.spinner("🤖 AI 診斷擬合品質中..."):
                try:
                    analysis = analyze_fit_with_llm(mmm, data, nvidia_key)
                    st.session_state["fit_analysis"] = analysis
                except Exception as e:
                    st.session_state["fit_analysis"] = f"（AI 分析失敗：{e}）"
    except Exception as e:
        progress_bar.empty()
        status_text.empty()
        st.error(f"擬合失敗：{e}")
        st.stop()

# ── 擬合結果（如果已擬合）──────────────────────────────────────────────────
if "mmm" in st.session_state:
    mmm = st.session_state["mmm"]
    config = st.session_state.get("fit_config", {})

    st.divider()
    st.subheader("擬合結果診斷")

    # 發散次數
    n_div = mmm.idata["sample_stats"]["diverging"].sum().item()
    if n_div == 0:
        st.success(f"✓ 發散次數：{n_div}（採樣成功）")
    else:
        st.warning(f"⚠ 發散次數：{n_div}（考慮提高 target_accept）")

    # 後驗預測圖
    st.markdown("**後驗預測 vs 實際值**")
    with st.expander("💡 怎麼判斷擬合效果？"):
        st.markdown("""
- ✅ 實際值（黑線）大部分落在預測區間（藍色陰影）內
- ✅ 預測均值（藍線）緊跟實際值趨勢
- ❌ 黑線常常在陰影外 → 模型需要改進（試試增加 draws 或調整先驗）
        """)

    fig = plot_posterior_predictive(mmm, data)
    st.pyplot(fig)

    # AI 擬合診斷（擬合後自動產生）
    if "fit_analysis" in st.session_state:
        st.divider()
        st.subheader("🤖 AI 擬合診斷")
        st.markdown(st.session_state["fit_analysis"])
    elif not os.environ.get("NVIDIA_API_KEY"):
        st.divider()
        st.caption("💡 設定 `NVIDIA_API_KEY` 環境變數後，擬合完成將自動產生 AI 擬合診斷。")

    st.divider()
    st.success("✅ 模型擬合完成！")
    st.page_link("pages/03_頻道貢獻.py", label="前往「頻道貢獻」分析各頻道效果 →", icon="📊")
else:
    if saved_model_exists():
        st.info("💾 有存檔的模型，請點擊上方「⚡ 載入上次擬合結果」跳過採樣，或重新擬合覆蓋存檔。")
    else:
        st.info("👆 點擊上方「🚀 開始擬合模型」按鈕，擬合完成後會自動存檔，下次重啟免重跑。")
