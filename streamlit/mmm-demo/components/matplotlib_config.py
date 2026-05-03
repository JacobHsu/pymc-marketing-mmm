"""Matplotlib runtime configuration for Streamlit demo charts."""

from __future__ import annotations

from pathlib import Path

import matplotlib
from matplotlib import font_manager


_FONT_FILES = (
    r"C:\Windows\Fonts\msjh.ttc",
    r"C:\Windows\Fonts\msyh.ttc",
    r"C:\Windows\Fonts\NotoSansTC-VF.ttf",
    r"C:\Windows\Fonts\simsun.ttc",
)


def configure_matplotlib_fonts() -> None:
    """Configure Matplotlib to render Chinese labels on Windows."""
    font_names: list[str] = []
    for font_file in _FONT_FILES:
        path = Path(font_file)
        if not path.exists():
            continue
        font_manager.fontManager.addfont(str(path))
        font_names.append(font_manager.FontProperties(fname=str(path)).get_name())

    if font_names:
        matplotlib.rcParams["font.sans-serif"] = font_names + list(matplotlib.rcParams["font.sans-serif"])
        matplotlib.rcParams["font.family"] = "sans-serif"

    matplotlib.rcParams["axes.unicode_minus"] = False
