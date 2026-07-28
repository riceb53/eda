import matplotlib.pyplot as plt

from .style import remove_spines


def _plot(kind, x, y, ax=None, **kwargs):
    ax = ax or plt.gca()
    getattr(ax, kind)(x, y, **kwargs)
    return remove_spines(ax)


def line(x, y, ax=None, **kwargs):
    kwargs.setdefault("linewidth", 4)
    return _plot("plot", x, y, ax=ax, **kwargs)


def scatter(x, y, ax=None, **kwargs):
    return _plot("scatter", x, y, ax=ax, **kwargs)


def bar(x, y, ax=None, **kwargs):
    return _plot("bar", x, y, ax=ax, **kwargs)
