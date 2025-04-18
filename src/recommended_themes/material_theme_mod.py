# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# Gitlab: https://gitlab.com/D4nitrix13
# Email: danielperezdev@proton.me

from typing import Dict, Any
from toml import loads

material_theme_mod: Dict[str, Any] = loads(s = """\
    # Colors (Material Theme)

    # Default colors
    [colors.primary]
    background = '#1e282d'
    foreground = '#c4c7d1'

    # Normal colors
    [colors.normal]
    black   = '#666666'
    red     = '#eb606b'
    green   = '#c3e88d'
    yellow  = '#f7eb95'
    blue    = '#80cbc4'
    magenta = '#ff2f90'
    cyan    = '#aeddff'
    white   = '#ffffff'

    # Bright colors
    [colors.bright]
    black   = '#a1a1a1'
    red     = '#eb606b'
    green   = '#c3e88d'
    yellow  = '#f7eb95'
    blue    = '#7dc6bf'
    magenta = '#6c71c4'
    cyan    = '#35434d'
    white   = '#ffffff'
    """
)