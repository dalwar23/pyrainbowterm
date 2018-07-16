# pyrainbowterm
pyrainbowterm - Smart custom print function with color and log information support.
Available in python 2.7.x and >3.2

:copyright: Copyright 2018 Dalwar Hossain

:scroll: License: MIT

This python package uses `print_function` from `__future__` module. To know more about `__future__.print_function`
please see this [documentation](https://docs.python.org/2/library/__future__.html)

#### Currently Supported Foreground Colors
- Black (black)
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
- Black (black)
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
- Information (info)
- Error (error)
- Warning (warn)
- Hint (hint)
- Debug (debug)

#### Setup
```python
python setup.py install
```

#### Usage Example
```python
from __future__ import print_function
from pyraibowterm import *
print(value1, value2, sep='-', end='\n', file=sys.stdout,
      color='red', bg_color='orange', text_format='bold', log_type='info')

```

#### Sample Screen Capture
![Sample Screen Capture](https://github.com/dharif23/xtermcolors/blob/master/images/xtermcolors.png)

#### Bug Report
Please report bugs at -

:email: dalwar.hossain@protonmail.com