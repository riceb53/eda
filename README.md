# eda

Utilities for modifying and styling matplotlib charts.

## Installation

```bash
pip install eda
```

## Usage

```python
import matplotlib.pyplot as plt
from eda.style import remove_spines

fig, ax = plt.subplots()
ax.plot([1, 2, 3], [1, 4, 9])
remove_spines(ax)
```

## Development

```bash
pip install -e ".[dev]"
pytest
```
