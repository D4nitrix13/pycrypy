# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# Gitlab: https://gitlab.com/D4nitrix13
# Email: danielperezdev@proton.me

from typing import Dict, Any
from toml import loads

github_light_high_contrast: Dict[str, Any] = loads(s = """\
    # (Github Light High Contrast) Colors for Alacritty

    # Default colors
    [colors.primary]
    background = '#ffffff'
    foreground = '#010409'

    # Cursor colors
    [colors.cursor]
    text = '#ffffff'
    cursor = '#0e1116'

    # Normal colors
    [colors.normal]
    black = '#0e1116'
    red = '#a0111f'
    green = '#024c1a'
    yellow = '#3f2200'
    blue = '#0349b4'
    magenta = '#622cbc'
    cyan = '#1b7c83'
    white = '#66707b'

    # Bright colors
    [colors.bright]
    black = '#4b535d'
    red = '#86061d'
    green = '#055d20'
    yellow = '#4e2c00'
    blue = '#1168e3'
    magenta = '#622cbc'
    cyan = '#1b7c83'
    white = '#66707b'
    """
)