# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# Gitlab: https://gitlab.com/D4nitrix13
# Email: danielperezdev@proton.me

from typing import Dict, Any
from toml import loads

seashells: Dict[str, Any] = loads(s = """\
    # Colors (SeaShells)
    # Source  https//raw.githubusercontent.com/mbadolato/iTerm2-Color-Schemes/master/schemes/SeaShells.itermcolors

    # Default colors
    [colors.primary]
    background = '#061923'
    foreground = '#e5c49e'

    [colors.cursor]
    text = '#061822'
    cursor = '#feaf3c'

    [colors.selection]
    text = '#ffe9d7'
    background = '#265b75'

    # Normal colors
    [colors.normal]
    black = '#1d485f'
    red = '#db662d'
    green = '#008eab'
    yellow = '#feaf3c'
    blue = '#255a62'
    magenta = '#77dbf4'
    cyan = '#5fb1c2'
    white = '#e5c49e'

    # Bright colors
    [colors.bright]
    black = '#545d65'
    red = '#dd998a'
    green = '#739da8'
    yellow = '#fedaae'
    blue = '#0bc7e3'
    magenta = '#c6e8f1'
    cyan = '#97b9c0'
    white = '#ffe9d7'
    """
)