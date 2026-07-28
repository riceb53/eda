# brianeda

Matplotlib-based plotting for pandas DataFrames.

## Installation

```bash
pip install brianeda
```

## Usage

```python
import pandas as pd
from brianeda import line

df = pd.DataFrame({"x": [1, 2, 3], "y": [1, 4, 9]})
line(df, "x", "y")
```

`line`, `scatter`, and `bar` all take a DataFrame and two column names, plot
onto an `Axes` (creating one via `plt.gca()` if `ax` isn't passed), and
return the `Axes` for further customization.

### Boxplots with a mood

`boxplot` draws one box per numeric column and colors them from a palette
chosen by `mood`:

```python
from brianeda import boxplot

boxplot(df, mood="excited")            # all numeric columns
boxplot(df, columns=["a", "b"], mood="sad")
```

Available moods (`brianeda.MOODS`): sad, excited, silly, calm, angry, happy,
mysterious, romantic, energetic, gloomy, playful, serene, bold, dreamy,
fierce, cheerful, melancholy, tropical, icy, earthy.

## Development

```bash
pip install -e ".[dev]"   # build + twine for packaging
```
