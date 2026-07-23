import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from brianeda.style import remove_spines


def test_remove_spines_hides_requested_spines():
    fig, ax = plt.subplots()
    remove_spines(ax, spines=("top", "right"))
    assert not ax.spines["top"].get_visible()
    assert not ax.spines["right"].get_visible()
    assert ax.spines["left"].get_visible()
