# brianeda

Matplotlib-based plotting for plain Python lists.

## Installation

```bash
pip install brianeda
```

## Usage

```python
from brianeda import line

line([1, 2, 3], [1, 4, 9])
```

`line`, `scatter`, and `bar` all take two sequences (`x`, `y`), plot onto an
`Axes` (creating one via `plt.gca()` if `ax` isn't passed), and return the
`Axes` for further customization.

### Boxplots with a mood

`boxplot` takes one sequence (a single box) or a list of sequences (one box
each) and colors them from a palette chosen by `mood`:

```python
from brianeda import boxplot

boxplot([[1, 2, 3, 9], [2, 3, 5, 6]], labels=["a", "b"], mood="excited")
```

Available moods (`brianeda.MOODS`): sad, excited, silly, calm, angry, happy,
mysterious, romantic, energetic, gloomy, playful, serene, bold, dreamy,
fierce, cheerful, melancholy, tropical, icy, earthy.

## Development

```bash
pip install -e ".[dev]"   # build + twine for packaging
```
