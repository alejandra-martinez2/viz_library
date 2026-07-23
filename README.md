# viz_library

this is a visualization library

A tiny Python package that makes matplotlib plots look more artistic, with almost no extra code.

## Install

```bash
pip install -e .
```

## Usage

```python
import matplotlib.pyplot as plt
import viz_library as vl

vl.use_style("sunset")  # or "pastel", "ink"

fig, ax = plt.subplots()
vl.gradient_fill(ax, x, y, color="#f8b195")
```

## What's included

- `use_style(name)` — applies an artsy color theme ("sunset", "pastel", "ink") to all following plots.
- `gradient_fill(ax, x, y, color, alpha)` — a line plot with a smooth gradient fill underneath.
- `glow_line(ax, x, y, color, layers, linewidth)` — a line with a soft neon glow.
- `rounded_bars(ax, x, heights, width, color, radius)` — a bar chart with rounded tops.
