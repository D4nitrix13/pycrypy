# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# Gitlab: https://gitlab.com/D4nitrix13
# Email: danielperezdev@proton.me

from typing import Dict, Any
from toml import loads

github_light_default: Dict[str, Any] = loads(s = """\
    # github Alacritty Colors

    # Default colors
    [colors.primary]
    background = '#ffffff'
    foreground = '#0E1116'

    # Normal colors
    [colors.normal]
    black   = '#24292f'
    red     = '#cf222e'
    green   = '#116329'
    yellow  = '#4d2d00'
    blue    = '#0969da'
    magenta = '#8250df'
    cyan    = '#1b7c83'
    white   = '#6e7781'

    # Bright colors
    [colors.bright]
    black   = '#57606a'
    red     = '#a40e26'
    green   = '#1a7f37'
    yellow  = '#633c01'
    blue    = '#218bff'
    magenta = '#a475f9'
    cyan    = '#3192aa'
    white   = '#8c959f'

    [[colors.indexed_colors]]
    index = 16
    color = '#d18616'

    [[colors.indexed_colors]]
    index = 17
    color = '#a40e26'
    """
)