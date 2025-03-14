# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# Gitlab: https://gitlab.com/D4nitrix13
# Email: danielperezdev@proton.me

from typing import Dict, Any
from toml import loads

pastel_dark: Dict[str, Any] = loads(s = """\
    # From iTerm2 Pastel Dark theme

    # Default colors
    [colors.primary]
    background = '#000000'
    foreground = '#C7C7C7'

    # Cursor colors
    [colors.cursor]
    text    = '#FFFEFF'
    cursor  = '#FFB472'

    # Normal colors
    [colors.normal]
    black    = '#616161'
    red      = '#FF8272'
    green    = '#B4FA72'
    yellow   = '#FEFDC2'
    blue     = '#A5D5FE'
    magenta  = '#FF8FFD'
    cyan     = '#D0D1FE'
    white    = '#F1F1F1'

    # Bright colors
    [colors.bright]
    black    = '#8E8E8E'
    red      = '#FFC4BD'
    green    = '#D6FCB9'
    yellow   = '#FEFDD5'
    blue     = '#C1E3FE'
    magenta  = '#FFB1FE'
    cyan     = '#E5E6FE'
    white    = '#FFFEFF'
    """
)