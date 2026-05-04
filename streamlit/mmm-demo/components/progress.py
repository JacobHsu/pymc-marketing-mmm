"""側邊欄流程進度指示器，並以 CSS 鎖定尚未可用的頁面連結。"""

import streamlit as st


def render_sidebar_progress() -> None:
    """渲染側邊欄步驟進度，並注入 CSS 使未解鎖頁面無法點擊。

    步驟順序：
        1. 資料總覽  — 資料載入後即可用（auto）
        2. 模型擬合  — 資料載入後即可用（auto）
        3. 頻道貢獻  — 需先完成模型擬合（mmm in session_state）
        4. 預算最佳化 — 需先完成模型擬合（mmm in session_state）

    Streamlit multi-page 側邊欄 li 順序：
        1 = app.py（主頁）
        2 = 01_資料總覽
        3 = 02_模型擬合
        4 = 03_頻道貢獻  ← 鎖定
        5 = 04_預算最佳化 ← 鎖定
    """
    has_model = "mmm" in st.session_state

    # 隱藏右上角 Deploy 按鈕（本機學習用途不需要）
    st.markdown(
        "<style>[data-testid='stAppDeployButton'] { display: none; }</style>",
        unsafe_allow_html=True,
    )

    # 固定 CSS：將第 1 個 nav 項目「app」顯示文字改為「導覽」
    rename_css = """
    [data-testid="stSidebarNav"] ul li:first-child a span {
        visibility: hidden;
        font-size: 0;
    }
    [data-testid="stSidebarNav"] ul li:first-child a span::before {
        content: "導覽";
        visibility: visible;
        font-size: 1rem;
    }
    """
    st.markdown(f"<style>{rename_css}</style>", unsafe_allow_html=True)

    # 注入 CSS：模型未完成時，鎖定第 4、5 個導覽項目
    if not has_model:
        locked_css = """
        [data-testid="stSidebarNav"] ul li:nth-child(4) a,
        [data-testid="stSidebarNav"] ul li:nth-child(5) a {
            pointer-events: none !important;
            opacity: 0.35 !important;
            cursor: not-allowed !important;
            color: #999 !important;
        }
        [data-testid="stSidebarNav"] ul li:nth-child(4) a::after,
        [data-testid="stSidebarNav"] ul li:nth-child(5) a::after {
            content: " 🔒";
            font-size: 0.75em;
            color: #aaa;
        }
        """
        st.markdown(f"<style>{locked_css}</style>", unsafe_allow_html=True)

    # 側邊欄視覺進度列
    has_data = "data" in st.session_state

    steps = [
        ("資料總覽", has_data),
        ("模型擬合", has_model),
        ("頻道貢獻", has_model),
        ("預算最佳化", has_model),
    ]

    st.sidebar.divider()
    st.sidebar.markdown("**📋 流程進度**")

    # 決定每步狀態：done / active / locked
    #   步驟 1, 2：資料就緒即 active；model done 即 done
    #   步驟 3, 4：model done 即 active（=done）；否則 locked
    statuses = []
    statuses.append("done" if has_data else "active")
    statuses.append("done" if has_model else "active")
    statuses.append("done" if has_model else "locked")
    statuses.append("done" if has_model else "locked")

    icons = {"done": "✅", "active": "▶️", "locked": "🔒"}
    colors = {"done": "#2e7d32", "active": "#1565c0", "locked": "#9e9e9e"}

    lines = []
    for i, ((label, _), status) in enumerate(zip(steps, statuses), 1):
        icon = icons[status]
        color = colors[status]
        lines.append(
            f'<div style="color:{color};margin:2px 0">{icon} {i}. {label}</div>'
        )

    st.sidebar.markdown("\n".join(lines), unsafe_allow_html=True)
