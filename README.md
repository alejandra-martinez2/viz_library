# viz_library

this is a visualization library

A tiny Python package that makes matplotlib plots look artsy — cherry-cola vintage, with almost no extra code.

## Install

```bash
pip install -e .
```

## Usage

```python
import matplotlib.pyplot as plt
import viz_library as vl

vl.use_style()

fig, ax = plt.subplots()
vl.gradient_fill(ax, x, y)
vl.lace_trim(ax)
vl.buckle(ax)
```

## What's included

- `use_style()` — applies the cherry theme (vintage cream paper, deep cherry red, black) to all following plots.
- `gradient_fill(ax, x, y, color, alpha)` — a line plot with a smooth gradient fill underneath.
- `rounded_bars(ax, x, heights, width, color, edge, radius)` — a bar chart with rounded, glossy tops.
- `stacked_bars(ax, x, series, colors, width)` — a stacked column chart from a list of value series.
- `combo_chart(ax, x, bars, line, bar_color, line_color, width)` — a bar-and-line combo chart on a single shared y-axis.
- `grain(ax, amount, color, alpha, seed)` — faint vintage film-grain speckle over an axes.
- `lace_trim(ax, color, scallops, size)` — a scalloped lace trim along the bottom edge of an axes.
- `buckle(ax, xy, width, height, color)` — a small belt-buckle glyph decoration above an axes.
