"""viz_library: cherry-cola vintage matplotlib plots, minimal effort."""

from .styles import CHERRY, use_style
from .effects import (
    gradient_fill, rounded_bars, stacked_bars, combo_chart, grain, lace_trim, buckle,
)

__all__ = [
    "CHERRY", "use_style", "gradient_fill", "rounded_bars", "stacked_bars",
    "combo_chart", "grain", "lace_trim", "buckle",
]
__version__ = "0.3.0"
