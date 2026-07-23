# eda

Matplotlib-based plotting for pandas DataFrames.

## Installation

```bash
pip install brianeda
```

## Usage

```python
import pandas as pd
from eda import line

df = pd.DataFrame({"x": [1, 2, 3], "y": [1, 4, 9]})
line(df, "x", "y")
```

`line`, `scatter`, and `bar` all take a DataFrame and two column names, plot
onto an `Axes` (creating one via `plt.gca()` if `ax` isn't passed), and
return the `Axes` for further customization.

## Development

```bash
pip install -e ".[dev]"
pytest
```
