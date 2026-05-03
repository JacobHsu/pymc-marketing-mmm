"""圖表函數：封裝所有 Matplotlib/Plotly 視覺化邏輯。"""

from __future__ import annotations

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import arviz as az
import numpy as np

from components.matplotlib_config import configure_matplotlib_fonts

configure_matplotlib_fonts()


def plot_time_series(data: pd.DataFrame, date_col: str, value_col: str, title: str, color: str = "C0") -> plt.Figure:
    """繪製時間序列折線圖。"""
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.plot(data[date_col], data[value_col], color=color, linewidth=2)
    ax.set(title=title, xlabel="日期", ylabel=value_col)
    ax.tick_params(axis="x", rotation=30)
    fig.tight_layout()
    return fig


def plot_channel_overview(data: pd.DataFrame, date_col: str, channel_cols: list[str], target_col: str) -> plt.Figure:
    """繪製目標變數 + 各頻道的多面板時間序列圖。"""
    n_rows = len(channel_cols) + 1
    fig, axes = plt.subplots(n_rows, 1, figsize=(12, 3 * n_rows), sharex=True)

    axes[0].plot(data[date_col], data[target_col], color="black", linewidth=2)
    axes[0].set(ylabel="銷售額", title="目標變數：銷售額")

    colors = [f"C{i}" for i in range(len(channel_cols))]
    for i, (ch, color) in enumerate(zip(channel_cols, colors)):
        axes[i + 1].plot(data[date_col], data[ch], color=color, linewidth=2)
        axes[i + 1].set(ylabel="花費", title=f"頻道 {ch}（廣告花費）")

    axes[-1].set(xlabel="日期")
    fig.tight_layout()
    return fig


def plot_spend_distribution(data: pd.DataFrame, channel_cols: list[str]) -> plt.Figure:
    """繪製各頻道花費分布的箱形圖。"""
    fig, ax = plt.subplots(figsize=(8, 4))
    spend_data = [data[ch].values for ch in channel_cols]
    ax.boxplot(spend_data, labels=channel_cols, patch_artist=True)
    ax.set(title="各頻道花費分布", xlabel="頻道", ylabel="花費（標準化）")
    fig.tight_layout()
    return fig


def plot_spend_share_pie(data: pd.DataFrame, channel_cols: list[str]) -> plt.Figure:
    """繪製各頻道花費佔比的圓餅圖。"""
    shares = data[channel_cols].sum()
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.pie(shares, labels=channel_cols, autopct="%1.1f%%", startangle=90, colors=[f"C{i}" for i in range(len(channel_cols))])
    ax.set_title("各頻道花費佔比")
    return fig


def plot_posterior_predictive(mmm, data: pd.DataFrame) -> plt.Figure:
    """繪製後驗預測 vs 實際值的比較圖。"""
    fig, ax = plt.subplots(figsize=(12, 5))
    date = mmm.model.coords["date"]

    ax.plot(date, mmm.y, color="black", linewidth=2, label="實際銷售")
    ax.plot(
        date,
        mmm.posterior_predictive.y_original_scale.mean(("chain", "draw")),
        color="C0",
        linewidth=2,
        label="模型預測均值",
    )
    for hdi_prob in (0.94, 0.5):
        az.plot_hdi(
            date,
            mmm.posterior_predictive.y_original_scale,
            hdi_prob=hdi_prob,
            smooth=False,
            ax=ax,
            color="C0",
            fill_kwargs={"alpha": 0.3 if hdi_prob == 0.94 else 0.5, "label": f"{hdi_prob:.0%} HDI"},
        )
    ax.legend()
    ax.set(title="模型擬合效果（後驗預測）", xlabel="日期", ylabel="銷售額")
    ax.tick_params(axis="x", rotation=30)
    fig.tight_layout()
    return fig


def plot_channel_contribution_over_time(mmm) -> plt.Figure:
    """繪製各頻道貢獻隨時間的變化。"""
    post = mmm.idata.posterior
    date = mmm.model.coords["date"]
    channel_cols = mmm.channel_columns

    fig, ax = plt.subplots(figsize=(12, 5))
    for i, ch in enumerate(channel_cols):
        mean_contrib = post["channel_contribution_original_scale"].sel(channel=ch).mean(("chain", "draw"))
        ax.fill_between(date, mean_contrib, alpha=0.6, label=f"頻道 {ch}", color=f"C{i}")

    ax.set(title="各頻道銷售貢獻（時間序列）", xlabel="日期", ylabel="銷售貢獻")
    ax.legend()
    ax.tick_params(axis="x", rotation=30)
    fig.tight_layout()
    return fig


def plot_roas_bar(roas_df: pd.DataFrame) -> plt.Figure:
    """繪製各頻道 ROAS 比較圖。"""
    fig, ax = plt.subplots(figsize=(8, 4))
    bars = ax.bar(roas_df["頻道"], roas_df["ROAS"], color=[f"C{i}" for i in range(len(roas_df))])
    ax.bar_label(bars, labels=[f"{v:.2f}x" for v in roas_df["ROAS"]], padding=3)
    ax.set(title="各頻道 ROAS（廣告花費回報率）", xlabel="頻道", ylabel="ROAS（銷售額 / 花費）")
    ax.axhline(1, color="red", linestyle="--", alpha=0.5, label="ROAS = 1（保本）")
    ax.legend()
    fig.tight_layout()
    return fig


def plot_waterfall(mmm) -> plt.Figure:
    """繪製貢獻瀑布圖。"""
    result = mmm.plot.waterfall_components_decomposition(original_scale=True)
    # API 回傳 (fig, ax) tuple 或單純 fig，統一取 fig
    return result[0] if isinstance(result, tuple) else result
