# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# Gitlab: https://gitlab.com/D4nitrix13
# Email: danielperezdev@proton.me

from typing import Dict, Any
from toml import loads

github_light_tritanopia: Dict[str, Any] = loads(s = """\
    # (Github Light Tritanopia) Colors for Alacritty

    # Default colors
    [colors.primary]
    background = '#ffffff'
    foreground = '#1b1f24'

    # Cursor colors
    [colors.cursor]
    text = '#ffffff'
    cursor = '#24292f'

    # Normal colors
    [colors.normal]
    black = '#24292f'
    red = '#cf222e'
    green = '#0550ae'
    yellow = '#4d2d00'
    blue = '#0969da'
    magenta = '#8250df'
    cyan = '#1b7c83'
    white = '#6e7781'

    # Bright colors
    [colors.bright]
    black = '#57606a'
    red = '#a40e26'
    green = '#0969da'
    yellow = '#633c01'
    blue = '#218bff'
    magenta = '#8250df'
    cyan = '#1b7c83'
    white = '#6e7781'
    """
)