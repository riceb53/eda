from importlib.metadata import PackageNotFoundError, version

from .boxplot import MOODS, boxplot
from .plot import bar, line, scatter
from .style import remove_spines

try:
    __version__ = version("brianeda")
except PackageNotFoundError:
    __version__ = "0.0.0"

__all__ = ["bar", "boxplot", "line", "scatter", "remove_spines", "MOODS", "__version__"]
