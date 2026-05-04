"""AI 資料分析：使用 NVIDIA NIM API 分析 MMM 數據，提供行銷洞察。"""

from __future__ import annotations

from typing import TYPE_CHECKING

import numpy as np
import pandas as pd

if TYPE_CHECKING:
    from openai import OpenAI
    from pymc_marketing.mmm.multidimensional import MMM

_NL = "\n"


def _make_client(api_key: str) -> OpenAI:
    """建立 NVIDIA NIM OpenAI 相容客戶端。"""
    from openai import OpenAI

    return OpenAI(base_url="https://integrate.api.nvidia.com/v1", api_key=api_key)


def _compute_fit_metrics(mmm: MMM, data: pd.DataFrame) -> dict[str, float | int]:
    """計算 MCMC 擬合品質指標。"""
    y_true = data["y"].values
    pp = mmm.idata["posterior_predictive"]["y"]

    sample_dims = [d for d in pp.dims if d in ("chain", "draw", "sample")]
    y_pred_mean = pp.mean(dim=sample_dims).values.flatten()
    n = min(len(y_true), len(y_pred_mean))
    y_true, y_pred_mean = y_true[:n], y_pred_mean[:n]

    ss_res = float(np.sum((y_true - y_pred_mean) ** 2))
    ss_tot = float(np.sum((y_true - y_true.mean()) ** 2))

    y_low = pp.quantile(0.05, dim=sample_dims).values.flatten()[:n]
    y_high = pp.quantile(0.95, dim=sample_dims).values.flatten()[:n]

    return {
        "mae": float(np.mean(np.abs(y_true - y_pred_mean))),
        "mape": float(
            np.mean(np.abs((y_true - y_pred_mean) / np.where(y_true == 0, 1, y_true))) * 100
        ),
        "r2": 1 - ss_res / ss_tot if ss_tot > 0 else float("nan"),
        "coverage": float(np.mean((y_true >= y_low) & (y_true <= y_high)) * 100),
        "n_div": int(mmm.idata["sample_stats"]["diverging"].sum().item()),
        "draws_used": int(pp.sizes.get("draw", pp.sizes.get("sample", 0))),
    }


def analyze_roas_with_llm(roas_df: pd.DataFrame, api_key: str) -> str:
    """將 ROAS 數據傳給 LLM，回傳繁體中文行銷洞察。

    使用 NVIDIA NIM API（OpenAI 相容），模型：meta/llama-3.3-70b-instruct。
    """
    rows = [
        f"  - {row['頻道']}：ROAS={row['ROAS']:.2f}x，"
        f"貢獻銷售額={row['總貢獻（銷售額）']:,.0f}，"
        f"總花費={row['總花費']:,.4f}"
        for _, row in roas_df.iterrows()
    ]
    data_text = _NL.join(rows)
    prompt = f"""你是一位資深行銷分析師，請根據以下 Media Mix Modeling（MMM）模型的估計結果，提供繁體中文分析。

各廣告頻道效益數據：
{data_text}

ROAS 說明：ROAS = 廣告帶來的銷售額 / 廣告花費。ROAS > 1 代表正向回報，越高越好。

請提供以下分析（條列式，約 150-200 字）：
1. **表現最佳頻道**：ROAS 最高的頻道，建議加碼投資
2. **表現待改善頻道**：ROAS 偏低的頻道，需重新評估策略
3. **預算分配建議**：根據 ROAS 排名，給出具體的預算調整方向
4. **一句話總結**：整體媒體組合的效率評估"""

    response = _make_client(api_key).chat.completions.create(
        model="meta/llama-3.3-70b-instruct",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=600,
        temperature=0.3,
    )
    return response.choices[0].message.content


def analyze_fit_with_llm(mmm: MMM, data: pd.DataFrame, api_key: str) -> str:
    """計算擬合品質指標後傳給 LLM，回傳繁體中文擬合診斷。"""
    m = _compute_fit_metrics(mmm, data)

    if m["draws_used"] < 500:
        prompt = f"""你是一位貝葉斯統計專家，請用繁體中文回覆以下情況。

本次 MMM 模型採樣次數（draws）為 {m["draws_used"]}，低於最低建議值 500。
MCMC 在採樣不足時尚未收斂，所有指標（R²={m["r2"]:.2f}、MAPE={m["mape"]:.0f}%、覆蓋率={m["coverage"]:.0f}%）都是無效的，不代表模型或資料有問題。

請用 2–3 句話說明：
1. 這些指標為什麼現在沒有意義（MCMC 未收斂）
2. 建議把 draws 調整到多少（正式分析建議 500，完整分析建議 1000）
3. 模型和資料本身是沒問題的，不需要修改設定

語氣要正面，不要讓人誤以為模型壞了。"""
    else:
        prompt = f"""你是一位貝葉斯統計專家，請根據以下 MMM 模型擬合指標，用繁體中文評估模型品質。

擬合指標：
  - R²（決定係數）：{m["r2"]:.3f}（越接近 1 越好）
  - MAE（平均絕對誤差）：{m["mae"]:.2f}
  - MAPE（平均絕對百分比誤差）：{m["mape"]:.1f}%
  - 90% 預測區間覆蓋率：{m["coverage"]:.1f}%（理想值接近 90%）
  - MCMC 發散次數：{m["n_div"]}（理想值為 0）
  - 採樣次數（draws）：{m["draws_used"]}

請提供以下診斷（條列式，約 150 字）：
1. **整體擬合評估**：模型好不好？給一個簡單結論
2. **需要注意的問題**：哪些指標不理想？代表什麼
3. **改善建議**：應該調整哪些參數"""

    response = _make_client(api_key).chat.completions.create(
        model="meta/llama-3.3-70b-instruct",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500,
        temperature=0.3,
    )
    return response.choices[0].message.content
