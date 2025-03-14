# Colors (Ayu Light)

# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# Gitlab: https://gitlab.com/D4nitrix13
# Email: danielperezdev@proton.me

from typing import Dict, Any
from toml import loads

ayu_light: Dict[str, Any] = loads(s = """\
    # Default colors - taken from ayu-colors
    [colors.primary]
    background = '#FCFCFC'
    foreground = '#5C6166'

    # Normal colors - taken from ayu-iTerm
    [colors.normal]
    black   = '#010101'
    red     = '#e7666a'
    green   = '#80ab24'
    yellow  = '#eba54d'
    blue    = '#4196df'
    magenta = '#9870c3'
    cyan    = '#51b891'
    white   = '#c1c1c1'

    # Bright colors - pastel lighten 0.1 <normal> except black lighten with 0.2
    [colors.bright]
    black   = '#343434'
    red     = '#ee9295'
    green   = '#9fd32f'
    yellow  = '#f0bc7b'
    blue    = '#6daee6'
    magenta = '#b294d2'
    cyan    = '#75c7a8'
    white   = '#dbdbdb'
    """
)