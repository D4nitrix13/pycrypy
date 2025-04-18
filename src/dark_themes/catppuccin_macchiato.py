# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# Gitlab: https://gitlab.com/D4nitrix13
# Email: danielperezdev@proton.me

from typing import Dict, Any
from toml import loads

catppuccin_macchiato: Dict[str, Any] = loads(s = """\
    # Default colors
    [colors.primary]
    background = '#24273A' # base
    foreground = '#CAD3F5' # text
    # Bright and dim foreground colors
    dim_foreground = '#CAD3F5' # text
    bright_foreground = '#CAD3F5' # text

    # Cursor colors
    [colors.cursor]
    text = '#24273A' # base
    cursor = '#F4DBD6' # rosewater

    [colors.vi_mode_cursor]
    text = '#24273A' # base
    cursor = '#B7BDF8' # lavender

    # Search colors
    [colors.search.matches]
    foreground = '#24273A' # base
    background = '#A5ADCB' # subtext0

    [colors.search.focused_match]
    foreground = '#24273A' # base
    background = '#A6DA95' # green

    [colors.footer_bar]
    foreground = '#24273A' # base
    background = '#A5ADCB' # subtext0

    # Keyboard regex hints
    [colors.hints.start]
    foreground = '#24273A' # base
    background = '#EED49F' # yellow

    [colors.hints.end]
    foreground = '#24273A' # base
    background = '#A5ADCB' # subtext0

    # Selection colors
    [colors.selection]
    text = '#24273A' # base
    background = '#F4DBD6' # rosewater

    # Normal colors
    [colors.normal]
    black = '#494D64' # surface1
    red = '#ED8796' # red
    green = '#A6DA95' # green
    yellow = '#EED49F' # yellow
    blue = '#8AADF4' # blue
    magenta = '#F5BDE6' # pink
    cyan = '#8BD5CA' # teal
    white = '#B8C0E0' # subtext1

    # Bright colors
    [colors.bright]
    black = '#5B6078' # surface2
    red = '#ED8796' # red
    green = '#A6DA95' # green
    yellow = '#EED49F' # yellow
    blue = '#8AADF4' # blue
    magenta = '#F5BDE6' # pink
    cyan = '#8BD5CA' # teal
    white = '#A5ADCB' # subtext0

    # Dim colors
    [colors.dim]
    black = '#494D64' # surface1
    red = '#ED8796' # red
    green = '#A6DA95' # green
    yellow = '#EED49F' # yellow
    blue = '#8AADF4' # blue
    magenta = '#F5BDE6' # pink
    cyan = '#8BD5CA' # teal
    white = '#B8C0E0' # subtext1
    """
)