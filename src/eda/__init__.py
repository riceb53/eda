from importlib.metadata import PackageNotFoundError, version

from .style import remove_spines

try:
    __version__ = version("eda")
except PackageNotFoundError:
    __version__ = "0.0.0"

__all__ = ["remove_spines", "__version__"]
