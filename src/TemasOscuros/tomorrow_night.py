# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# Gitlab: https://gitlab.com/D4nitrix13
# Email: danielperezdev@proton.me

from typing import Dict, Any
from toml import loads

tomorrow_night: Dict[str, Any] = loads(s = """\
    # Colors (Tomorrow Night)

    # Default colors
    [colors.primary]
    background = '#1d1f21'
    foreground = '#c5c8c6'

    [colors.cursor]
    text = '#1d1f21'
    cursor = '#ffffff'

    # Normal colors
    [colors.normal]
    black   = '#1d1f21'
    red     = '#cc6666'
    green   = '#b5bd68'
    yellow  = '#e6c547'
    blue    = '#81a2be'
    magenta = '#b294bb'
    cyan    = '#70c0ba'
    white   = '#373b41'

    # Bright colors
    [colors.bright]
    black   = '#666666'
    red     = '#ff3334'
    green   = '#9ec400'
    yellow  = '#f0c674'
    blue    = '#81a2be'
    magenta = '#b77ee0'
    cyan    = '#54ced6'
    white   = '#282a2e'
    """
)