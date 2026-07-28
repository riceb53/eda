from itertools import cycle

import matplotlib.pyplot as plt

from .style import remove_spines

# Each mood maps to a color palette; the boxes cycle through its colors.
MOODS = {
    "sad": ["#4a6fa5", "#6b8cae", "#93a9c9"],
    "excited": ["#ff5e5b", "#ffb400", "#ff8c42"],
    "silly": ["#ff6fd8", "#7afcff", "#feff9c"],
    "calm": ["#a8dadc", "#88c9bf", "#c7e9c0"],
    "angry": ["#8b0000", "#c1121f", "#e63946"],
    "happy": ["#ffd166", "#ffcb47", "#f4a261"],
    "mysterious": ["#3a015c", "#4f0147", "#35012c"],
    "romantic": ["#ffb3c6", "#ff8fab", "#fb6f92"],
    "energetic": ["#f72585", "#7209b7", "#4361ee"],
    "gloomy": ["#495057", "#6c757d", "#adb5bd"],
    "playful": ["#ff595e", "#ffca3a", "#8ac926"],
    "serene": ["#cdb4db", "#bde0fe", "#a2d2ff"],
    "bold": ["#d00000", "#ffba08", "#3f88c5"],
    "dreamy": ["#e0aaff", "#c77dff", "#9d4edd"],
    "fierce": ["#03071e", "#dc2f02", "#f48c06"],
    "cheerful": ["#ffbe0b", "#fb5607", "#ff006e"],
    "melancholy": ["#5c677d", "#7d8597", "#979dac"],
    "tropical": ["#00afb9", "#fed9b7", "#f07167"],
    "icy": ["#caf0f8", "#90e0ef", "#00b4d8"],
    "earthy": ["#606c38", "#a68a64", "#7f5539"],
}


def boxplot(data, labels=None, mood="calm", ax=None, **kwargs):
    if mood not in MOODS:
        raise ValueError(f"unknown mood {mood!r}; choose from {sorted(MOODS)}")
    ax = ax or plt.gca()
    result = ax.boxplot(data, patch_artist=True, **kwargs)
    for box, color in zip(result["boxes"], cycle(MOODS[mood])):
        box.set_facecolor(color)
    if labels is not None:
        ax.set_xticks(range(1, len(labels) + 1))
        ax.set_xticklabels(labels)
    return remove_spines(ax)
