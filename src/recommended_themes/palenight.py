# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# Gitlab: https://gitlab.com/D4nitrix13
# Email: danielperezdev@proton.me

from typing import Dict, Any
from toml import loads

palenight: Dict[str, Any] = loads(s = """\
    # iTerm2 Material Design - Palenight theme for Alacritty
    # Source  https//github.com/JonathanSpeek/palenight-iterm2

    # Default colors
    [colors.primary]
    background = '#292d3e'
    foreground = '#d0d0d0'

    # Normal colors
    [colors.normal]
    black   = '#292d3e'
    red     = '#f07178'
    green   = '#c3e88d'
    yellow  = '#ffcb6b'
    blue    = '#82aaff'
    magenta = '#c792ea'
    cyan    = '#89ddff'
    white   = '#d0d0d0'

    # Bright colors
    [colors.bright]
    black   = '#434758'
    red     = '#ff8b92'
    green   = '#ddffa7'
    yellow  = '#ffe585'
    blue    = '#9cc4ff'
    magenta = '#e1acff'
    cyan    = '#a3f7ff'
    white   = '#ffffff'
    """
)