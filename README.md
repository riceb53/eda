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

### Mood-colored line graphs

`multiline` plots several y-columns against one x-column, coloring each line
from the chosen `mood` palette and adding a legend:

```python
from brianeda import multiline

multiline(df, "x", ["y1", "y2", "y3"], mood="excited")
```

## Examples

### Pokémon TCG AI battle episodes

Per-episode scores are sequential, so a boxplot of the score columns and a
line graph of scores across episodes both work well:

```python
import kagglehub, glob, os
import pandas as pd
import matplotlib.pyplot as plt
from brianeda import boxplot, multiline

path = kagglehub.dataset_download("kaggle/pokemon-tcg-ai-battle-episodes-2026-07-26")
poke = pd.read_csv(glob.glob(os.path.join(path, "**/*.csv"), recursive=True)[0])

# distribution of each score column
boxplot(poke, columns=["avg_score", "min_score", "sum_score"], mood="excited")
plt.tight_layout(); plt.savefig("pokemon_boxplot.png"); plt.clf()

# scores across episodes
multiline(poke, "episode_id", ["avg_score", "min_score"], mood="excited")
plt.tight_layout(); plt.savefig("pokemon_lines.png")
```

### NYC Regents exams

This data is cross-sectional (one row per school/exam/year). Reshape it to
one column per subject for a per-subject boxplot, or aggregate by year for a
line graph:

```python
import kagglehub, glob, os
import pandas as pd
import matplotlib.pyplot as plt
from brianeda import boxplot, multiline

path = kagglehub.dataset_download("razanihababdellatif/nyc-regents-exam-dataset")
regents = pd.read_csv(glob.glob(os.path.join(path, "**/*.csv"), recursive=True)[0])
regents["Mean Score"] = pd.to_numeric(regents["Mean Score"], errors="coerce")
clean = regents.dropna(subset=["Mean Score"])

# one box per subject (reshape long -> wide, NaN-padded)
wide = (clean.assign(_i=clean.groupby("Regents Exam").cumcount())
             .pivot(index="_i", columns="Regents Exam", values="Mean Score"))
boxplot(wide, mood="melancholy")
plt.xticks(rotation=45, ha="right")
plt.tight_layout(); plt.savefig("regents_boxplot.png"); plt.clf()

# mean score per subject over time
yearly = clean.groupby(["Year", "Regents Exam"])["Mean Score"].mean().unstack().reset_index()
multiline(yearly, "Year", ["Algebra I", "Geometry"], mood="melancholy")
plt.tight_layout(); plt.savefig("regents_lines.png")
```

## Development

```bash
pip install -e ".[dev]"   # build + twine for packaging
```
