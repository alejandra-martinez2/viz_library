# viz_library

this is a visualization library

A tiny Python package that makes matplotlib plots look artsy — Y2K cherry-coquette-grunge, with almost no extra code.

## Install

```bash
pip install -e .
```

## Usage

```python
import matplotlib.pyplot as plt
import viz_library as vl

vl.use_style("cherry")  # or "coquette", "grunge"

fig, ax = plt.subplots()
vl.gradient_fill(ax, x, y)
```

## What's included

- `use_style(name)` — applies a theme to all following plots:
  - `"coquette"` — light, blush, lace (2000's, girly, soft)
  - `"cherry"` — vintage cream paper with deep cherry red and black
  - `"grunge"` — distressed charcoal with faded cherry and rust
- `gradient_fill(ax, x, y, color, alpha)` — a line plot with a smooth gradient fill underneath.
- `sparkle_line(ax, x, y, color, glitter, sparkles, seed)` — a line dusted with glitter star sparkles.
- `rounded_bars(ax, x, heights, width, color, edge, radius)` — a bar chart with rounded tops and a bow-black outline.
- `grain(ax, amount, color, alpha, seed)` — faint vintage film-grain speckle over an axes.
