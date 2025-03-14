# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# Gitlab: https://gitlab.com/D4nitrix13
# Email: danielperezdev@proton.me

from typing import Dict, Any
from toml import loads

bluish: Dict[str, Any] = loads(s = """\
    # Default colors
    [colors.primary]
    background = '#2c3640'
    foreground = '#297dd3'

    # Normal colors
    [colors.normal]
    black   = '#0b0b0c'
    red     = '#377fc4'
    green   = '#2691e7'
    yellow  = '#2090c1'
    blue    = '#2c5e87'
    magenta = '#436280'
    cyan    = '#547aa2'
    white   = '#536679'

    # Bright colors
    [colors.bright]
    black   = '#23272c'
    red     = '#66a5cc'
    green   = '#59b0f2'
    yellow  = '#4bb0d3'
    blue    = '#487092'
    magenta = '#50829e'
    cyan    = '#658795'
    white   = '#4d676b'
    """
)