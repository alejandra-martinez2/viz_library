"""viz_library: make matplotlib plots look artsy with minimal effort."""

from .styles import THEMES, use_style
from .effects import gradient_fill, glow_line, rounded_bars

__all__ = ["THEMES", "use_style", "gradient_fill", "glow_line", "rounded_bars"]
__version__ = "0.1.0"
