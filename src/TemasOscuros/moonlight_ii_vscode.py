# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# Gitlab: https://gitlab.com/D4nitrix13
# Email: danielperezdev@proton.me

from typing import Dict, Any
from toml import loads

moonlight_ii_vscode: Dict[str, Any] = loads(s = """\
    [colors.primary]
    background = '#1e2030'
    foreground = '#7f85a3'

    [colors.cursor]
    text   = '#7f85a3'
    cursor = '#808080'

    [colors.normal]
    black   = '#444a73'
    red     = '#ff5370'
    green   = '#4fd6be'
    yellow  = '#ffc777'
    blue    = '#3e68d7'
    magenta = '#fc7b7b'
    cyan    = '#86e1fc'
    white   = '#d0d0d0'

    [colors.bright]
    black   = '#828bb8'
    red     = '#ff98a4'
    green   = '#c3e88d'
    yellow  = '#ffc777'
    blue    = '#82aaff'
    magenta = '#ff966c'
    cyan    = '#b4f9f8'
    white   = '#5f8787'
    """
)