# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# Gitlab: https://gitlab.com/D4nitrix13
# Email: danielperezdev@proton.me

from typing import Dict, Any
from toml import loads

baitong: Dict[str, Any] = loads(s = """\
    # Colors (Baitong)

    [colors.primary]
    background = '#112a2a'
    foreground = '#33ff33'

    [colors.cursor]
    text = '#112a2a'
    cursor = '#ff00ff'

    [colors.vi_mode_cursor]
    text = '#112a2a'
    cursor = '#ff00ff'

    [colors.search]
    matches = { foreground = '#000000', background = '#1AE642' }
    focused_match = { foreground = '#000000', background = '#ff00ff' }

    [colors.hints]
    start = { foreground = '#1d1f21', background = '#1AE642' }
    end = { foreground = '#1AE642', background = '#1d1f21' }

    [colors.line_indicator]
    foreground = '#33ff33'
    background = '#1d1f21'

    [colors.footer_bar]
    background = '#731d8b'
    foreground = '#ffffff'

    [colors.selection]
    text = '#112a2a'
    background = '#1AE642'

    # Normal colors
    [colors.normal]
    black   = '#000000'
    red     = '#f77272'
    green   = '#33ff33'
    yellow  = '#1AE642'
    blue    = '#68FDFE'
    magenta = '#ff66ff'
    cyan    = '#87CEFA'
    white   = '#dbdbd9'

    # Bright colors
    [colors.bright]
    black   = '#ffffff'
    red     = '#f77272'
    green   = '#33ff33'
    yellow  = '#1AE642'
    blue    = '#68FDFE'
    magenta = '#ff66ff'
    cyan    = '#68FDFE'
    white   = '#dbdbd9'
    """
)