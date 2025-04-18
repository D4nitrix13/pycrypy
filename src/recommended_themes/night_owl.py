# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# Gitlab: https://gitlab.com/D4nitrix13
# Email: danielperezdev@proton.me

from typing import Dict, Any
from toml import loads

night_owl: Dict[str, Any] = loads(s = """\
    # Default colors
    [colors.primary]
    background = "#011627"
    foreground = "#d6deeb"

    # Cursor colors
    [colors.cursor]
    text = "CellBackground"
    cursor = "CellForeground"

    [colors.vi_mode_cursor]
    text = "CellBackground"
    cursor = "#22da6e"

    # Search colors
    [colors.search.matches]
    foreground = "#000000"
    background = "#22da6e"

    [colors.search.focused_match]
    foreground = "#ffffff"
    background = "#22da6e"

    [colors.footer_bar]
    foreground = "#ffffff"
    background = "#1d3b53"

    # Selection colors
    [colors.selection]
    text = "#ffffff"
    background = "#0d486e"

    # Normal colors
    [colors.normal]
    black = "#011627"
    red = "#EF5350"
    green = "#22da6e"
    yellow = "#c5e478"
    blue = "#82AAFF"
    magenta = "#C792EA"
    cyan = "#21c7a8"
    white = "#ffffff"

    # Bright colors
    [colors.bright]
    black = "#575656"
    red = "#EF5350"
    green = "#22da6e"
    yellow = "#ffeb95"
    blue = "#82AAFF"
    magenta = "#C792EA"
    cyan = "#7fdbca"
    white = "#ffffff"
    """
)