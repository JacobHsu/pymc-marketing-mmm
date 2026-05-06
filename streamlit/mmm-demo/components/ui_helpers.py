"""共用 UI helper — 在 st.title / st.markdown header 前置 Material Symbols 圖示。

Streamlit 的 st.title / st.header / st.subheader 不支援 icon= 參數，
但 Material Symbols Rounded 字型已由 Streamlit 本身全域載入（woff2 本地檔），
可透過 unsafe_allow_html 注入 <span> 取得相同圖示。

字型大小對齊 Streamlit theme (utils.D9m7Ykmm.js)：
  fontSizes  : threeXL=2.25rem, twoXL=1.75rem, xl=1.5rem
  iconSizes  : threeXL=2.3rem,  twoXL=1.8rem,  xl=1.5rem
"""

import streamlit as st

_ICON_SPAN = (
    "font-family:'Material Symbols Rounded';"
    "font-weight:400;font-style:normal;"
    "font-feature-settings:'liga';"
    "-webkit-font-feature-settings:'liga';"
    "user-select:none;display:block;line-height:1;"
)

_ROW = "display:flex;align-items:center;gap:{gap};margin:{margin};"
_TEXT = "margin:0;padding:0;line-height:1.2;font-family:inherit;"


def icon_title(icon: str, text: str, color: str = "#2563eb") -> None:
    """渲染帶 Material Symbol 的 h1 標題（對應 st.title）。"""
    st.markdown(
        f'<div style="{_ROW.format(gap="10px", margin="0 0 1rem 0")}'
        f'font-size:2.25rem;font-weight:700">'
        f'<span style="{_ICON_SPAN}font-size:2.25rem;color:{color}">{icon}</span>'
        f'<span style="{_TEXT}">{text}</span>'
        f'</div>',
        unsafe_allow_html=True,
    )


def icon_header(icon: str, text: str, color: str = "#334155") -> None:
    """渲染帶 Material Symbol 的 h2 標題（對應 st.header）。"""
    st.markdown(
        f'<div style="{_ROW.format(gap="8px", margin="0 0 0.75rem 0")}'
        f'font-size:1.75rem;font-weight:700">'
        f'<span style="{_ICON_SPAN}font-size:1.75rem;color:{color}">{icon}</span>'
        f'<span style="{_TEXT}">{text}</span>'
        f'</div>',
        unsafe_allow_html=True,
    )


def icon_subheader(icon: str, text: str, color: str = "#475569") -> None:
    """渲染帶 Material Symbol 的 h3 標題（對應 st.subheader）。"""
    st.markdown(
        f'<div style="{_ROW.format(gap="6px", margin="0 0 0.5rem 0")}'
        f'font-size:1.5rem;font-weight:600">'
        f'<span style="{_ICON_SPAN}font-size:1.5rem;color:{color}">{icon}</span>'
        f'<span style="{_TEXT}">{text}</span>'
        f'</div>',
        unsafe_allow_html=True,
    )
