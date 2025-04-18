# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# Gitlab: https://gitlab.com/D4nitrix13
# Email: danielperezdev@proton.me

from typing import Dict, Any
from toml import loads

iterm: Dict[str, Any] = loads(s = """\
    # Colors (iTerm 2 default theme)

    # Default colors
    [colors.primary]
    background = '#101421'
    foreground = '#fffbf6'

    # Normal colors
    [colors.normal]
    black   = '#2e2e2e'
    red     = '#eb4129'
    green   = '#abe047'
    yellow  = '#f6c744'
    blue    = '#47a0f3'
    magenta = '#7b5cb0'
    cyan    = '#64dbed'
    white   = '#e5e9f0'

    # Bright colors
    [colors.bright]
    black   = '#565656'
    red     = '#ec5357'
    green   = '#c0e17d'
    yellow  = '#f9da6a'
    blue    = '#49a4f8'
    magenta = '#a47de9'
    cyan    = '#99faf2'
    white   = '#ffffff'
    """
)