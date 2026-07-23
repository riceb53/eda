import matplotlib

matplotlib.use("Agg")
import pandas as pd

from brianeda.plot import line


def test_line_plots_dataframe_columns():
    df = pd.DataFrame({"x": [1, 2, 3], "y": [1, 4, 9]})
    ax = line(df, "x", "y")
    x_data, y_data = ax.lines[0].get_xdata(), ax.lines[0].get_ydata()
    assert list(x_data) == df["x"].tolist()
    assert list(y_data) == df["y"].tolist()


def test_line_is_thick_by_default_but_overridable():
    df = pd.DataFrame({"x": [1, 2, 3], "y": [1, 4, 9]})
    assert line(df, "x", "y").lines[-1].get_linewidth() == 4
    assert line(df, "x", "y", linewidth=1).lines[-1].get_linewidth() == 1
