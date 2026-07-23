from matplotlib.axes import Axes


def remove_spines(ax: Axes, spines=("top", "right")) -> Axes:
    for spine in spines:
        ax.spines[spine].set_visible(False)
    return ax
