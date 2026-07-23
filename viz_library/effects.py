"""Y2K cherry-coquette-grunge touches for any matplotlib axes."""

import numpy as np
import matplotlib.colors as mcolors
from matplotlib.patches import FancyBboxPatch, Polygon


def gradient_fill(ax, x, y, color="#d2042d", alpha=0.6):
    """Plot a line and fill underneath it with a cherry-cola gradient."""
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


def sparkle_line(ax, x, y, color="#c9838f", glitter="#ffd700", sparkles=40, seed=0):
    """Draw a line dusted with glitter-like star sparkles."""
    x, y = np.asarray(x, dtype=float), np.asarray(y, dtype=float)
    line, = ax.plot(x, y, color=color, linewidth=2, zorder=2)

    rng = np.random.default_rng(seed)
    idx = rng.choice(len(x), size=min(sparkles, len(x)), replace=False)
    sizes = rng.uniform(20, 90, size=idx.size)
    alphas = rng.uniform(0.5, 1.0, size=idx.size)
    ax.scatter(
        x[idx], y[idx], s=sizes, marker="*", color=glitter,
        edgecolors="#1c1c1c", linewidths=0.4, alpha=alphas, zorder=3,
    )
    return line


def rounded_bars(ax, x, heights, width=0.6, color="#c9838f", edge="#1c1c1c", radius=0.05):
    """Draw a coquette-style bar chart: rounded tops with a bow-black outline."""
    patches = []
    for xi, h in zip(x, heights):
        box = FancyBboxPatch(
            (xi - width / 2, 0), width, h,
            boxstyle=f"round,pad=0,rounding_size={radius}",
            facecolor=color, edgecolor=edge, linewidth=1.2,
        )
        ax.add_patch(box)
        patches.append(box)
    ax.set_xlim(min(x) - width, max(x) + width)
    ax.set_ylim(0, max(heights) * 1.15)
    return patches


def grain(ax, amount=400, color="#1c1c1c", alpha=0.04, seed=0):
    """Scatter faint vintage film-grain speckle across the axes."""
    rng = np.random.default_rng(seed)
    xlim, ylim = ax.get_xlim(), ax.get_ylim()
    xs = rng.uniform(*xlim, size=amount)
    ys = rng.uniform(*ylim, size=amount)
    sizes = rng.uniform(0.5, 3, size=amount)
    ax.scatter(xs, ys, s=sizes, color=color, alpha=alpha, zorder=10, linewidths=0)
