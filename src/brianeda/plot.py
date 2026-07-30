from itertools import cycle

import matplotlib.pyplot as plt

from .boxplot import MOODS
from .style import remove_spines


def _plot(kind, df, x, y, ax=None, **kwargs):
    ax = ax or plt.gca()
    getattr(ax, kind)(df[x], df[y], **kwargs)
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    return remove_spines(ax)


def line(df, x, y, ax=None, **kwargs):
    kwargs.setdefault("linewidth", 4)
    return _plot("plot", df, x, y, ax=ax, **kwargs)


def scatter(df, x, y, ax=None, **kwargs):
    return _plot("scatter", df, x, y, ax=ax, **kwargs)


def bar(df, x, y, ax=None, **kwargs):
    return _plot("bar", df, x, y, ax=ax, **kwargs)


def multiline(df, x, ys, mood="calm", ax=None, **kwargs):
    if mood not in MOODS:
        raise ValueError(f"unknown mood {mood!r}; choose from {sorted(MOODS)}")
    kwargs.setdefault("linewidth", 4)
    ax = ax or plt.gca()
    for col, color in zip(ys, cycle(MOODS[mood])):
        ax.plot(df[x], df[col], label=col, color=color, **kwargs)
    ax.set_xlabel(x)
    ax.legend()
    return remove_spines(ax)
