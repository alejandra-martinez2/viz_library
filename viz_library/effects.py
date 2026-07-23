"""Small artistic touches you can add to any matplotlib axes."""

import numpy as np
import matplotlib.colors as mcolors
from matplotlib.patches import FancyBboxPatch, Polygon


def gradient_fill(ax, x, y, color="#f67280", alpha=0.6):
    """Plot a line and fill underneath it with a top-to-bottom gradient."""
    x, y = np.asarray(x, dtype=float), np.asarray(y, dtype=float)
    line, = ax.plot(x, y, color=color, linewidth=2)

    z = np.empty((100, 1, 4))
    z[:, :, :3] = mcolors.to_rgb(color)
    z[:, :, 3] = np.linspace(0, alpha, 100)[:, None]

    ymin = min(0, y.min())
    ymax = y.max() * 1.1 if y.max() > 0 else y.max() * 0.9
    im = ax.imshow(
        z, aspect="auto", origin="lower", zorder=line.get_zorder() - 1,
        extent=[x.min(), x.max(), ymin, ymax],
    )

    verts = np.vstack([[x.min(), ymin], np.column_stack([x, y]), [x.max(), ymin]])
    clip = Polygon(verts, facecolor="none", edgecolor="none", closed=True)
    ax.add_patch(clip)
    im.set_clip_path(clip)
    return line, im


def glow_line(ax, x, y, color="#a2d2ff", layers=6, linewidth=2):
    """Draw a line with a soft neon-like glow around it."""
    for i in range(layers, 0, -1):
        ax.plot(x, y, color=color, linewidth=linewidth + i * 2, alpha=0.06)
    return ax.plot(x, y, color=color, linewidth=linewidth)[0]


def rounded_bars(ax, x, heights, width=0.6, color="#ffafcc", radius=0.05):
    """Draw a bar chart with friendly rounded tops instead of sharp corners."""
    patches = []
    for xi, h in zip(x, heights):
        box = FancyBboxPatch(
            (xi - width / 2, 0), width, h,
            boxstyle=f"round,pad=0,rounding_size={radius}",
            facecolor=color, edgecolor="none",
        )
        ax.add_patch(box)
        patches.append(box)
    ax.set_xlim(min(x) - width, max(x) + width)
    ax.set_ylim(0, max(heights) * 1.15)
    return patches
