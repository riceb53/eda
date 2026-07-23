import matplotlib.pyplot as plt

from .style import remove_spines


def _plot(kind, df, x, y, ax=None, **kwargs):
    ax = ax or plt.gca()
    getattr(ax, kind)(df[x], df[y], **kwargs)
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    return remove_spines(ax)


def line(df, x, y, ax=None, **kwargs):
    return _plot("plot", df, x, y, ax=ax, **kwargs)


def scatter(df, x, y, ax=None, **kwargs):
    return _plot("scatter", df, x, y, ax=ax, **kwargs)


def bar(df, x, y, ax=None, **kwargs):
    return _plot("bar", df, x, y, ax=ax, **kwargs)
