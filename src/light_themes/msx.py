# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# Gitlab: https://gitlab.com/D4nitrix13
# Email: danielperezdev@proton.me

from typing import Dict, Any
from toml import loads

msx: Dict[str, Any] = loads(s = """\
    # Colors (MSX-like)
    # Notice that MSX used blue as background so [bright] blue and [bright] black
    # are reversed in this theme. Also MSX had only 15 colors (color 0 was
    # transparent) so 'gray' (#CCCCCC) is used two times both as white and
    # bright black.

    # Default colors
    [colors.primary]
    background = '#5955E0'
    foreground = '#FFFFFF'

    # Normal colors
    [colors.normal]
    # It is 'dark blue' not black
    black = '#5955E0'
    red = '#B95E51'
    green = '#3AA241'
    yellow = '#CCC35E'
    # It is 'black' not blue
    blue = '#000000'
    # It is 'medium red' not magenta
    magenta = '#DB6559'
    # It is 'medium green' not cyan
    cyan = '#3EB849'
    # It is 'gray' not white
    white = '#CCCCCC'

    # Bright colors
    [colors.bright]
    # It is 'light blue' not bright black
    black = '#8076F1'
    red = '#FF897D'
    green = '#74D07D'
    yellow = '#DED087'
    # It is 'gray' not bright blue
    blue = '#CCCCCC'
    # It is 'magenta' not bright magenta
    magenta = '#B766B5'
    # It is 'cyan' not bright cyan
    cyan = '#65DBEF'
    white = '#FFFFFF'
    """
)
