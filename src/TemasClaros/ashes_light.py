# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# Gitlab: https://gitlab.com/D4nitrix13
# Email: danielperezdev@proton.me

from typing import Dict, Any
from toml import loads

ashes_light: Dict[str, Any] = loads(s = """\
    [colors.primary]
    background = '#f3f4f5'
    foreground = '#565e65'

    [colors.cursor]
    text = '#f3f4f5'
    cursor = '#565e65'

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