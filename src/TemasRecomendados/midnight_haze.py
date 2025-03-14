# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# Gitlab: https://gitlab.com/D4nitrix13
# Email: danielperezdev@proton.me

from typing import Dict, Any
from toml import loads

midnight_haze: Dict[str, Any] = loads(s = """\
    # Midnight Haze theme
    # Source https//github.com/hafiz-muhammad/midnight-haze-alacritty-theme

    # Default colors
    [colors.primary]
    background = '#0c0c16'
    foreground = '#d8dee9'

    # Normal colors
    [colors.normal]
    black   = '#2c2c3d'
    red     = '#ff6e6e'
    green   = '#9ec875'
    yellow  = '#ffa759'
    blue    = '#70a7d4'
    magenta = '#d291e0'
    cyan    = '#96e0e0'
    white   = '#d8dee9'

    # Bright colors
    [colors.bright]
    black   = '#414166'
    red     = '#ff8d8d'
    green   = '#b3d987'
    yellow  = '#ffc57f'
    blue    = '#9bb3d3'
    magenta = '#ffa1ff'
    cyan    = '#9cd8d8'
    white   = '#ffffff'
    """
)