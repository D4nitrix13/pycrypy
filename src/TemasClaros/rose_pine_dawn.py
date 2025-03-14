# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# Gitlab: https://gitlab.com/D4nitrix13
# Email: danielperezdev@proton.me

from typing import Dict, Any
from toml import loads

rose_pine_dawn: Dict[str, Any] = loads(s = """\
    [colors.primary]
    background = '#faf4ed'
    foreground = '#575279'

    [colors.cursor]
    text = '#575279'
    cursor = '#cecacd'

    [colors.vi_mode_cursor]
    text = '#575279'
    cursor = '#cecacd'

    [colors.selection]
    text = '#575279'
    background = '#dfdad9'

    [colors.normal]
    black = '#f2e9e1'
    red = '#b4637a'
    green = '#286983'
    yellow = '#ea9d34'
    blue = '#56949f'
    magenta = '#907aa9'
    cyan = '#d7827e'
    white = '#575279'

    [colors.bright]
    black = '#9893a5'
    red = '#b4637a'
    green = '#286983'
    yellow = '#ea9d34'
    blue = '#56949f'
    magenta = '#907aa9'
    cyan = '#d7827e'
    white = '#575279'

    [colors.hints]
    start = { foreground = '#797593', background = '#fffaf3' }
    end = { foreground = '#9893a5', background = '#fffaf3' }
    """
)