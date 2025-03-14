# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# Gitlab: https://gitlab.com/D4nitrix13
# Email: danielperezdev@proton.me

from typing import Dict, Any
from toml import loads

night_owlish_light: Dict[str, Any] = loads(s = """\
    # Colors (Night Owlish Light)

    [colors.primary]
    background = '#ffffff'
    foreground = '#403f53'

    [colors.normal]
    black = '#011627'
    red = '#d3423e'
    green = '#2aa298'
    yellow = '#daaa01'
    blue = '#4876d6'
    magenta = '#403f53'
    cyan = '#08916a'
    white = '#7a8181'

    [colors.bright]
    black = '#7a8181'
    red = '#f76e6e'
    green = '#49d0c5'
    yellow = '#dac26b'
    blue = '#5ca7e4'
    magenta = '#697098'
    cyan = '#00c990'
    white = '#989fb1'

    [colors.cursor]
    cursor = '#403f53'
    text = '#fbfbfb'

    [colors.selection]
    background = '#f2f2f2'
    text = '#403f53'
    """
)