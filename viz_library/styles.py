"""Y2K cherry-coquette-grunge matplotlib themes, applied as global rcParams."""

import matplotlib.pyplot as plt

cycler = plt.cycler

THEMES = {
    # light, girly, 2000's coquette: bows, lace, blush
    "coquette": {
        "figure.facecolor": "#fdf1f5",
        "axes.facecolor": "#fff8fa",
        "axes.edgecolor": "#d8a7b1",
        "axes.labelcolor": "#8a5b64",
        "text.color": "#8a5b64",
        "xtick.color": "#8a5b64",
        "ytick.color": "#8a5b64",
        "grid.color": "#eec9d2",
        "grid.alpha": 0.6,
        "axes.grid": True,
        "font.family": "serif",
        "axes.prop_cycle": cycler(
            color=["#f4a6c6", "#f7cad0", "#e8b4bc", "#c9838f", "#fadadd"]
        ),
    },
    # cherry-cola vintage: cream paper, deep cherry red, black
    "cherry": {
        "figure.facecolor": "#fff8ec",
        "axes.facecolor": "#fffaf0",
        "axes.edgecolor": "#1c1c1c",
        "axes.labelcolor": "#1c1c1c",
        "text.color": "#1c1c1c",
        "xtick.color": "#1c1c1c",
        "ytick.color": "#1c1c1c",
        "grid.color": "#d2042d",
        "grid.alpha": 0.15,
        "axes.grid": True,
        "font.family": "serif",
        "axes.prop_cycle": cycler(
            color=["#9e1b32", "#d2042d", "#1c1c1c", "#6e2c1e", "#c0c0c0"]
        ),
    },
    # coach-jacket grunge: distressed charcoal, faded cherry, rust
    "grunge": {
        "figure.facecolor": "#171412",
        "axes.facecolor": "#1e1a17",
        "axes.edgecolor": "#e4ded0",
        "axes.labelcolor": "#e4ded0",
        "text.color": "#e4ded0",
        "xtick.color": "#e4ded0",
        "ytick.color": "#e4ded0",
        "grid.color": "#6e2c1e",
        "grid.alpha": 0.35,
        "axes.grid": True,
        "font.family": "monospace",
        "axes.prop_cycle": cycler(
            color=["#c97c8b", "#8b0000", "#e4ded0", "#6e2c1e", "#a89f91"]
        ),
    },
}


def use_style(name="cherry"):
    """Apply a Y2K cherry-coquette-grunge theme globally to all following plots.

    Parameters
    ----------
    name : str
        One of "coquette" (light, blush, lace), "cherry" (vintage cream +
        cherry red), or "grunge" (distressed charcoal + faded cherry).
    """
    if name not in THEMES:
        raise ValueError(f"Unknown theme '{name}'. Choose from {list(THEMES)}")
    plt.rcParams.update(THEMES[name])
