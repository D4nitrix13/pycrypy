# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# Gitlab: https://gitlab.com/D4nitrix13
# Email: danielperezdev@proton.me

from typing import Dict, Any
from toml import loads

remedy_dark: Dict[str, Any] = loads(s = """\
    # Default colors
    [colors.primary]
    background = '#2c2b2a'
    foreground = '#f9e7c4'

    dim_foreground    = '#685E4A'
    bright_foreground = '#1C1508'

    # Normal colors
    [colors.normal]
    black   = '#282a2e'
    red     = '#a54242'
    green   = '#8c9440'
    yellow  = '#de935f'
    blue    = '#5f819d'
    magenta = '#85678f'
    cyan    = '#5e8d87'
    white   = '#707880'

    # Bright colors
    [colors.bright]
    black   = '#373b41'
    red     = '#cc6666'
    green   = '#b5bd68'
    yellow  = '#f0c674'
    blue    = '#81a2be'
    magenta = '#b294bb'
    cyan    = '#8abeb7'
    white   = '#c5c8c6'
    """
)