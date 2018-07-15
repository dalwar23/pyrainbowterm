# xtermcolors
xtermcolors - Smart print function with color and log information support.
Available in python 2.7.x

:copyright: Copyright 2018 Dalwar Hossain

:scroll: License: MIT

This python package uses `print_function` from `__future__` module. To know more about `__future__.print_function`
please visit this [documentation](https://docs.python.org/2/library/__future__.html)

#### Currently supported Foreground Colors
- Red (red)
- Green (green)
- Orange (orange)
- Blue (blue)
- Purple (purple)
- Cyan (cyan)
- Light Gray (light_gray)
- Dark Gray (dark_gray)
- Light Red (light_red)
- Light green (light_green)
- Yellow (yellow)
- Light Blue (light_blue)
- Pink (pink)
- Light Cyan (light_cyan)

#### Currently Supported Background Colors
- Gray (gray)
- Red (red)
- Green (green)
- Blue (blue)
- Orange (orange)
- Purple (purple)
- Cyan (cyan)
- Light Gray (light_gray)

#### Currently Supported Text Formats
- Bold (bold)
- Dark (dark)
- Underline (underline)
- Blink (blink) *\[depends on OS and terminal\]*
- Reverse (reverse)
- Strike Through (strike_through)
- Concealed (concealed)

#### Currently Supported Log Types
- Info (info)
- Error (error)
- Warn (warn)
- Hint (hint)
- Debug (debug)

#### Usage Example
```python
from __future__ import print_function
from xtermcolors import *
print(value1, value2, sep='-', end='\n', file=sys.stdout,
      color='red', bg_color='orange', text_format='bold', log_type='info')

```

#### Bug Report
Please report any bug to the author at below email address

:email: dalwar.hossain@protonmail.com