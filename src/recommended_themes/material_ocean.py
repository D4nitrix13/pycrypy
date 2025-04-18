# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# Gitlab: https://gitlab.com/D4nitrix13
# Email: danielperezdev@proton.me

from typing import Dict, Any
from toml import loads

material_ocean: Dict[str, Any] = loads(s = """\
    # Themes Colors (material-ocean)

    # Default colors material-ocean
    [colors.primary]
    background = '#0f101a'
    foreground = '#c5c9de'

    # Normal colors material-ocean
    [colors.normal]
    black = '#181a29'
    red = '#F07178'
    green = '#cdea9f'
    yellow = '#ffd47e'
    blue = '#93bbff'
    magenta = '#d3a7ee'
    cyan = '#98e4ff'
    white = '#bfd5de'

    # Bright colors material-ocean
    [colors.bright]
    black = '#282a40'
    red = '#eb7f84'
    green = '#e0ffad'
    yellow = '#ffee7e'
    blue = '#a3c5ff'
    magenta = '#d6afed'
    cyan = '#98fffd'
    white = '#d1e5ed'
    """
)