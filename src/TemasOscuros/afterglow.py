# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# Gitlab: https://gitlab.com/D4nitrix13
# Email: danielperezdev@proton.me

from typing import Dict, Any
from toml import loads

afterglow: Dict[str, Any] = loads(s = """\
    # Default colors
    [colors.primary]
    background = '#2c2c2c'
    foreground = '#d6d6d6'

    dim_foreground    = '#dbdbdb'
    bright_foreground = '#d9d9d9'

    # Cursor colors
    [colors.cursor]
    text   = '#2c2c2c'
    cursor = '#d9d9d9'

    # Normal colors
    [colors.normal]
    black   = '#1c1c1c'
    red     = '#bc5653'
    green   = '#909d63'
    yellow  = '#ebc17a'
    blue    = '#7eaac7'
    magenta = '#aa6292'
    cyan    = '#86d3ce'
    white   = '#cacaca'

    # Bright colors
    [colors.bright]
    black   = '#636363'
    red     = '#bc5653'
    green   = '#909d63'
    yellow  = '#ebc17a'
    blue    = '#7eaac7'
    magenta = '#aa6292'
    cyan    = '#86d3ce'
    white   = '#f7f7f7'

    # Dim colors
    [colors.dim]
    black   = '#232323'
    red     = '#74423f'
    green   = '#5e6547'
    yellow  = '#8b7653'
    blue    = '#556b79'
    magenta = '#6e4962'
    cyan    = '#5c8482'
    white   = '#828282'
    """
)