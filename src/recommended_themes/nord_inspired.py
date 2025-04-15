# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# Gitlab: https://gitlab.com/D4nitrix13
# Email: danielperezdev@proton.me

from typing import Dict, Any
from toml import loads

nord_inspired: Dict[str, Any] = loads(s = """\
    # Themes Colors (nord-inspired)

    # Default colors nord-inspired
    [colors.primary]
    background = '#2e3440'
    foreground = '#d8dee9'
    
    # Normal colors nord-inspired
    [colors.normal]
    black = '#3b4252'
    red = '#bf616a'
    green = '#a3be8c'
    yellow = '#ebcb8b'
    blue = '#81a1c1'
    magenta ='#b48ead'
    cyan = '#88c0d0'
    white = '#bfd5de'
    
    # Bright colors nord-inspired
    [colors.bright]
    black = '#434c5e'
    red = '#bf616a'
    green = '#a3be8c'
    yellow = '#ebcb8b'
    blue = '#81a1c1'
    magenta = '#b48ead'
    cyan = '#88c0d0'
    white = '#e5e9f0'
    """
)