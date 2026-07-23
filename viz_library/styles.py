"""Artsy matplotlib themes, applied as global rcParams."""

import matplotlib.pyplot as plt

cycler = plt.cycler

THEMES = {
    "sunset": {
        "figure.facecolor": "#2b1055",
        "axes.facecolor": "#2b1055",
        "axes.edgecolor": "#f8b195",
        "axes.labelcolor": "#f8f1e7",
        "text.color": "#f8f1e7",
        "xtick.color": "#f8f1e7",
        "ytick.color": "#f8f1e7",
        "grid.color": "#f8b195",
        "grid.alpha": 0.15,
        "axes.grid": True,
        "font.family": "serif",
        "axes.prop_cycle": cycler(
            color=["#f67280", "#f8b195", "#c06c84", "#6c5b7b", "#355c7d"]
        ),
    },
    "pastel": {
        "figure.facecolor": "#fdf6f0",
        "axes.facecolor": "#fdf6f0",
        "axes.edgecolor": "#c9ada7",
        "axes.labelcolor": "#4a4a4a",
        "text.color": "#4a4a4a",
        "xtick.color": "#4a4a4a",
        "ytick.color": "#4a4a4a",
        "grid.color": "#c9ada7",
        "grid.alpha": 0.3,
        "axes.grid": True,
        "font.family": "sans-serif",
        "axes.prop_cycle": cycler(
            color=["#ffafcc", "#a2d2ff", "#bde0fe", "#cdb4db", "#ffc8dd"]
        ),
    },
    "ink": {
        "figure.facecolor": "#111111",
        "axes.facecolor": "#111111",
        "axes.edgecolor": "#eeeeee",
        "axes.labelcolor": "#eeeeee",
        "text.color": "#eeeeee",
        "xtick.color": "#eeeeee",
        "ytick.color": "#eeeeee",
        "grid.color": "#555555",
        "grid.alpha": 0.4,
        "axes.grid": True,
        "font.family": "monospace",
        "axes.prop_cycle": cycler(color=["#ffffff", "#cccccc", "#999999"]),
    },
}


def use_style(name="sunset"):
    """Apply an artsy theme globally, so all following plots pick it up.

    Parameters
    ----------
    name : str
        One of "sunset", "pastel", or "ink".
    """
    if name not in THEMES:
        raise ValueError(f"Unknown theme '{name}'. Choose from {list(THEMES)}")
    plt.rcParams.update(THEMES[name])
