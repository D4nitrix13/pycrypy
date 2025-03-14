# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# Gitlab: https://gitlab.com/D4nitrix13
# Email: danielperezdev@proton.me

from typing import Dict, Any
from toml import loads

omni: Dict[str, Any] = loads(s = """\
    [colors.primary]
    background = '#191622'
    foreground = '#e1e1e6'

    [colors.cursor]
    text = '#191622'
    cursor = '#f8f8f2'

    [colors.normal]
    black = '#000000'
    red = '#ff5555'
    green = '#50fa7b'
    yellow = '#effa78'
    blue = '#bd93f9'
    magenta = '#ff79c6'
    cyan = '#8d79ba'
    white = '#bfbfbf'

    [colors.bright]
    black = '#4d4d4d'
    red = '#ff6e67'
    green = '#5af78e'
    yellow = '#eaf08d'
    blue = '#caa9fa'
    magenta = '#ff92d0'
    cyan = '#aa91e3'
    white = '#e6e6e6'

    [colors.dim]
    black = '#000000'
    red = '#a90000'
    green = '#049f2b'
    yellow = '#a3b106'
    blue = '#530aba'
    magenta = '#bb006b'
    cyan = '#433364'
    white = '#5f5f5f'
    """
)