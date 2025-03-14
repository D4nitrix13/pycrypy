# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# Gitlab: https://gitlab.com/D4nitrix13
# Email: danielperezdev@proton.me

from typing import Dict, Any
from toml import loads

nightfly: Dict[str, Any] = loads(s = """\
    # Source https://github.com/bluz71/vim-nightfly-colors

    [colors.bright]
    black = "#7c8f8f"
    blue = "#82aaff"
    cyan = "#7fdbca"
    green = "#21c7a8"
    magenta = "#ae81ff"
    red = "#ff5874"
    white = "#d6deeb"
    yellow = "#ecc48d"

    [colors.cursor]
    cursor = "#9ca1aa"
    text = "#080808"

    [colors.normal]
    black = "#1d3b53"
    blue = "#82aaff"
    cyan = "#7fdbca"
    green = "#a1cd5e"
    magenta = "#c792ea"
    red = "#fc514e"
    white = "#a1aab8"
    yellow = "#e3d18a"

    [colors.primary]
    background = "#011627"
    bright_foreground = "#eeeeee"
    foreground = "#bdc1c6"

    [colors.selection]
    background = "#b2ceee"
    text = "#080808"
    """
)