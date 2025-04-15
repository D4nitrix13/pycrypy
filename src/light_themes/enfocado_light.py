# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# Gitlab: https://gitlab.com/D4nitrix13
# Email: danielperezdev@proton.me

from typing import Dict, Any
from toml import loads

enfocado_light: Dict[str, Any] = loads(s = """\
    # Theme: enfocado_light
    # Source:  https://github.com/wuelnerdotexe/vim-enfocado

    # Default colors
    [colors.primary]
    background = '#ffffff'
    foreground = '#474747'

    # Normal colors
    [colors.normal]
    black   = '#282828'
    red     = '#d6000c'
    green   = '#1d9700'
    yellow  = '#c49700'
    blue    = '#0064e4'
    magenta = '#dd0f9d'
    cyan    = '#00ad9c'
    white   = '#cdcdcd'

    # Bright colors
    [colors.bright]
    black   = '#878787'
    red     = '#df0000'
    green   = '#008400'
    yellow  = '#af8500'
    blue    = '#0054cf'
    magenta = '#c7008b'
    cyan    = '#009a8a'
    white   = '#ebebeb'
    """
)