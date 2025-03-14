# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# Gitlab: https://gitlab.com/D4nitrix13
# Email: danielperezdev@proton.me

from typing import Dict, Any
from toml import loads

ashes_dark: Dict[str, Any] = loads(s = """\
    [colors.primary]
    background = '#1c2023'
    foreground = '#c7ccd1'

    [colors.cursor]
    text = '#1c2023'
    cursor = '#c7ccd1'

    [colors.normal]
    black   = '#1c2023'
    red     = '#c7ae95'
    green   = '#95c7ae'
    yellow  = '#aec795'
    blue    = '#ae95c7'
    magenta = '#c795ae'
    cyan    = '#95aec7'
    white   = '#c7ccd1'

    [colors.bright]
    black   = '#747c84'
    red     = '#c7ae95'
    green   = '#95c7ae'
    yellow  = '#aec795'
    blue    = '#ae95c7'
    magenta = '#c795ae'
    cyan    = '#95aec7'
    white   = '#f3f4f5'
    """
)