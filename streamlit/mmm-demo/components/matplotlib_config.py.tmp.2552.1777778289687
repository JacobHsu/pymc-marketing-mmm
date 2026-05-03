"""Matplotlib runtime configuration for Streamlit demo charts."""

from __future__ import annotations

from pathlib import Path

import matplotlib
from matplotlib import font_manager

# 打包字型（雲端 / 本機通用）
_BUNDLED_FONT = Path(__file__).parent.parent / "assets" / "fonts" / "msjh.ttc"

# 本機 Windows 備援
_WINDOWS_FONT_FILES = (
    r"C:\Windows\Fonts\msjh.ttc",
    r"C:\Windows\Fonts\msyh.ttc",
    r"C:\Windows\Fonts\NotoSansTC-VF.ttf",
    r"C:\Windows\Fonts\simsun.ttc",
)


def configure_matplotlib_fonts() -> None:
    """Configure Matplotlib to render Chinese labels on all platforms."""
    candidates: list[Path] = [_BUNDLED_FONT] + [Path(f) for f in _WINDOWS_FONT_FILES]

    font_names: list[str] = []
    for path in candidates:
        if not path.exists():
            continue
        font_manager.fontManager.addfont(str(path))
        font_names.append(font_manager.FontProperties(fname=str(path)).get_name())

    if font_names:
        matplotlib.rcParams["font.sans-serif"] = font_names + list(matplotlib.rcParams["font.sans-serif"])
        matplotlib.rcParams["font.family"] = "sans-serif"

    matplotlib.rcParams["axes.unicode_minus"] = False
