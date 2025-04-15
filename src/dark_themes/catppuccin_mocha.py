# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# Gitlab: https://gitlab.com/D4nitrix13
# Email: danielperezdev@proton.me

from typing import Dict, Any
from toml import loads

catppuccin_mocha: Dict[str, Any] = loads(s = """\
    [colors.primary]
    background = '#1E1E2E' # base
    foreground = '#CDD6F4' # text
    # Bright and dim foreground colors
    dim_foreground = '#CDD6F4' # text
    bright_foreground = '#CDD6F4' # text

    # Cursor colors
    [colors.cursor]
    text = '#1E1E2E' # base
    cursor = '#F5E0DC' # rosewater

    [colors.vi_mode_cursor]
    text = '#1E1E2E' # base
    cursor = '#B4BEFE' # lavender

    # Search colors
    [colors.search.matches]
    foreground = '#1E1E2E' # base
    background = '#A6ADC8' # subtext0

    [colors.search.focused_match]
    foreground = '#1E1E2E' # base
    background = '#A6E3A1' # green

    [colors.footer_bar]
    foreground = '#1E1E2E' # base
    background = '#A6ADC8' # subtext0

    # Keyboard regex hints
    [colors.hints.start]
    foreground = '#1E1E2E' # base
    background = '#F9E2AF' # yellow

    [colors.hints.end]
    foreground = '#1E1E2E' # base
    background = '#A6ADC8' # subtext0

    # Selection colors
    [colors.selection]
    text = '#1E1E2E' # base
    background = '#F5E0DC' # rosewater

    # Normal colors
    [colors.normal]
    black = '#45475A' # surface1
    red = '#F38BA8' # red
    green = '#A6E3A1' # green
    yellow = '#F9E2AF' # yellow
    blue = '#89B4FA' # blue
    magenta = '#F5C2E7' # pink
    cyan = '#94E2D5' # teal
    white = '#BAC2DE' # subtext1

    # Bright colors
    [colors.bright]
    black = '#585B70' # surface2
    red = '#F38BA8' # red
    green = '#A6E3A1' # green
    yellow = '#F9E2AF' # yellow
    blue = '#89B4FA' # blue
    magenta = '#F5C2E7' # pink
    cyan = '#94E2D5' # teal
    white = '#A6ADC8' # subtext0

    # Dim colors
    [colors.dim]
    black = '#45475A' # surface1
    red = '#F38BA8' # red
    green = '#A6E3A1' # green
    yellow = '#F9E2AF' # yellow
    blue = '#89B4FA' # blue
    magenta = '#F5C2E7' # pink
    cyan = '#94E2D5' # teal
    white = '#BAC2DE' # subtext1
    """
)