"""Cherry-cola vintage matplotlib theme, applied as global rcParams."""

import matplotlib.pyplot as plt

CHERRY = {
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
    "axes.prop_cycle": plt.cycler(
        color=["#9e1b32", "#d2042d", "#1c1c1c", "#6e2c1e", "#c0c0c0"]
    ),
}


def use_style():
    """Apply the cherry vintage theme globally to all following plots."""
    plt.rcParams.update(CHERRY)
