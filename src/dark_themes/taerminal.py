# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# Gitlab: https://gitlab.com/D4nitrix13
# Email: danielperezdev@proton.me

from typing import Dict, Any
from toml import loads

taerminal: Dict[str, Any] = loads(s = """\
    # Colors (Taerminal)

    # Default colors
    [colors.primary]
    background = '#26282a'
    foreground = '#f0f0f0'

    [colors.cursor]
    background = '#f0f0f0'
    foreground = '#26282a'

    # Normal colors
    [colors.normal]
    black   = '#26282a'
    red     = '#ff8878'
    green   = '#b4fb73'
    yellow  = '#fffcb7'
    blue    = '#8bbce5'
    magenta = '#ffb2fe'
    cyan    = '#a2e1f8'
    white   = '#f1f1f1'

    # Bright colors
    [colors.bright]
    black   = '#6f6f6f'
    red     = '#fe978b'
    green   = '#d6fcba'
    yellow  = '#fffed5'
    blue    = '#c2e3ff'
    magenta = '#ffc6ff'
    cyan    = '#c0e9f8'
    white   = '#ffffff'
    """
)