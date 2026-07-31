"""Cherry-cola vintage touches for any matplotlib axes."""

import numpy as np
import matplotlib.colors as mcolors
from matplotlib.patches import FancyBboxPatch, Polygon, Wedge


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


def rounded_bars(ax, x, heights, width=0.6, color="#9e1b32", edge="#1c1c1c", radius=0.05):
    """Draw a bar chart with glossy, rounded cherry tops."""
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


def stacked_bars(ax, x, series, colors=None, width=0.6):
    """Draw a stacked column chart from a list of equal-length value series."""
    colors = colors or ["#9e1b32", "#d2042d", "#6e2c1e", "#c0c0c0"]
    bottoms = np.zeros(len(x))
    for i, values in enumerate(series):
        values = np.asarray(values, dtype=float)
        ax.bar(
            x, values, bottom=bottoms, width=width,
            color=colors[i % len(colors)], edgecolor="#1c1c1c", linewidth=0.8,
        )
        bottoms += values
    ax.set_xlim(min(x) - width, max(x) + width)
    ax.set_ylim(0, bottoms.max() * 1.15)
    return bottoms


def combo_chart(ax, x, bars, line, bar_color="#9e1b32", line_color="#1c1c1c", width=0.6):
    """Draw a bar-and-line combo chart sharing a single y-axis."""
    ax.bar(x, bars, width=width, color=bar_color, edgecolor="#1c1c1c", linewidth=0.8, zorder=2)
    ax.plot(x, line, color=line_color, linewidth=2.5, marker="o", zorder=3)
    ax.set_xlim(min(x) - width, max(x) + width)
    ax.set_ylim(0, max(max(bars), max(line)) * 1.15)


def grain(ax, amount=400, color="#1c1c1c", alpha=0.04, seed=0):
    """Scatter faint vintage film-grain speckle across the axes."""
    rng = np.random.default_rng(seed)
    xlim, ylim = ax.get_xlim(), ax.get_ylim()
    xs = rng.uniform(*xlim, size=amount)
    ys = rng.uniform(*ylim, size=amount)
    sizes = rng.uniform(0.5, 3, size=amount)
    ax.scatter(xs, ys, s=sizes, color=color, alpha=alpha, zorder=10, linewidths=0)


def lace_trim(ax, color="#9e1b32", scallops=16, size=0.03):
    """Draw a scalloped lace trim hanging off the bottom edge of the axes."""
    for i in range(scallops):
        cx = (i + 0.5) / scallops
        wedge = Wedge(
            (cx, 0), size, 180, 360, transform=ax.transAxes,
            facecolor="none", edgecolor=color, linewidth=1.2, zorder=5, clip_on=False,
        )
        ax.add_patch(wedge)


def buckle(ax, xy=(0.06, 1.06), width=0.05, height=0.03, color="#1c1c1c"):
    """Draw a small belt-buckle glyph above the axes."""
    x0, y0 = xy
    frame = FancyBboxPatch(
        (x0 - width / 2, y0 - height / 2), width, height,
        boxstyle="round,pad=0.002,rounding_size=0.01", transform=ax.transAxes,
        facecolor="none", edgecolor=color, linewidth=1.6, zorder=6, clip_on=False,
    )
    ax.add_patch(frame)
    ax.plot(
        [x0, x0], [y0 - height / 2 - 0.01, y0 + height / 2 + 0.01],
        color=color, linewidth=1.6, transform=ax.transAxes, clip_on=False, zorder=6,
    )
    return frame
