# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# Gitlab: https://gitlab.com/D4nitrix13
# Email: danielperezdev@proton.me

from typing import Dict, Any
from toml import loads

pencil_dark: Dict[str, Any] = loads(s = """\
    # Colors (Pencil Dark)

    # Default Colors
    [colors.primary]
    background = '#212121'
    foreground = '#f1f1f1'

    # Normal colors
    [colors.normal]
    black   = '#212121'
    red     = '#c30771'
    green   = '#10a778'
    yellow  = '#a89c14'
    blue    = '#008ec4'
    magenta = '#523c79'
    cyan    = '#20a5ba'
    white   = '#e0e0e0'

    # Bright colors
    [colors.bright]
    black   = '#818181'
    red     = '#fb007a'
    green   = '#5fd7af'
    yellow  = '#f3e430'
    blue    = '#20bbfc'
    magenta = '#6855de'
    cyan    = '#4fb8cc'
    white   = '#f1f1f1'
    """
)