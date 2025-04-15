# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# Gitlab: https://gitlab.com/D4nitrix13
# Email: danielperezdev@proton.me

from typing import Dict, Any
from toml import loads

rose_pine_moon: Dict[str, Any] = loads(s = """\
    [colors.primary]
    background = '#232136'
    foreground = '#e0def4'

    [colors.cursor]
    text = '#e0def4'
    cursor = '#56526e'

    [colors.vi_mode_cursor]
    text = '#e0def4'
    cursor = '#56526e'

    [colors.selection]
    text = '#e0def4'
    background = '#44415a'
    [colors.normal]
    black = '#393552'
    red = '#eb6f92'
    green = '#3e8fb0'
    yellow = '#f6c177'
    blue = '#9ccfd8'
    magenta = '#c4a7e7'
    cyan = '#ea9a97'
    white = '#e0def4'

    [colors.bright]
    black = '#6e6a86'
    red = '#eb6f92'
    green = '#3e8fb0'
    yellow = '#f6c177'
    blue = '#9ccfd8'
    magenta = '#c4a7e7'
    cyan = '#ea9a97'
    white = '#e0def4'

    [colors.hints]
    start = { foreground = '#908caa', background = '#2a273f' }
    end = { foreground = '#6e6a86', background = '#2a273f' }
    """
)