# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# Gitlab: https://gitlab.com/D4nitrix13
# Email: danielperezdev@proton.me

from typing import Dict, Any
from toml import loads

gotham: Dict[str, Any] = loads(s = """\
    # Colors (Gotham)

    # Default colors
    [colors.primary]
    background = '#0a0f14'
    foreground = '#98d1ce'

    # Normal colors
    [colors.normal]
    black = '#0a0f14'
    red = '#c33027'
    green = '#26a98b'
    yellow = '#edb54b'
    blue = '#195465'
    magenta = '#4e5165'
    cyan = '#33859d'
    white = '#98d1ce'

    # Bright colors
    [colors.bright]
    black = '#10151b'
    red = '#d26939'
    green = '#081f2d'
    yellow = '#245361'
    blue = '#093748'
    magenta = '#888ba5'
    cyan = '#599caa'
    white = '#d3ebe9'
    """
)