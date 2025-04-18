# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# Gitlab: https://gitlab.com/D4nitrix13
# Email: danielperezdev@proton.me

from typing import Dict, Any
from toml import loads

ubuntu: Dict[str, Any] = loads(s = """\
    # 0x From the Ubuntu terminal color palette

    # 0x Default colors
    [colors.primary]
    background = '#300a24'
    foreground = '#eeeeec'

    # 0x Colors the cursor will use if `custom_cursor_colors` is true
    [colors.cursor]
    text = '#bbbbbb'
    cursor = '#b4d5ff'

    # 0x Normal colors
    [colors.normal]
    black   = '#2e3436'
    red     = '#cc0000'
    green   = '#4e9a06'
    yellow  = '#c4a000'
    blue    = '#3465a4'
    magenta = '#75507b'
    cyan    = '#06989a'
    white   = '#d3d7cf'

    # 0x Bright colors
    [colors.bright]
    black   = '#555753'
    red     = '#ef2929'
    green   = '#8ae234'
    yellow  = '#fce94f'
    blue    = '#729fcf'
    magenta = '#ad7fa8'
    cyan    = '#34e2e2'
    white   = '#eeeeec'
    """
)