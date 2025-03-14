# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# Gitlab: https://gitlab.com/D4nitrix13
# Email: danielperezdev@proton.me

from typing import Dict, Any
from toml import loads

nord_light: Dict[str, Any] = loads(s = """\
    # Colors (Nord light) theme based on https//github.com/nordtheme/alacritty/issues/28#issuecomment-1422225211

    # Default colors
    [colors.primary]
    background = '#ECEFF4'
    foreground = '#81A1C1'

    # Normal colors
    [colors.normal]
    black   = '#D8DEE9'
    red     = '#bf616a'
    green   = '#a3be8c'
    yellow  = '#D08770'
    blue    = '#81A1C1'
    magenta = '#B48EAD'
    cyan    = '#88C0D0'
    white   = '#4C566A'

    # Bright colors
    [colors.bright]
    black   = '#D8DEE9'
    red     = '#bf616a'
    green   = '#a3be8c'
    yellow  = '#D08770'
    blue    = '#D8DEE9'
    magenta = '#B48EAD'
    cyan    = '#8FBCBB'
    white   = '#D8DEE9'
    """
)