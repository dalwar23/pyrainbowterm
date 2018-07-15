# xtermcolors
xtermcolors - Smart print function with color and log information support.
Available in python 2.7.x

:copyright: 2018 Dalwar Hossain
:Licence: MIT

This **python package** uses `print_function` from `__future__` module. To know more about `__future__.print_function`
please visit [https://docs.python.org/2/library/__future__.html](https://docs.python.org/2/library/__future__.html)

#### Currently supported Foreground Colors
Red, Green, Orange, Blue,Purple, Cyan, Light Gray, Dark Gray, Light Red, Light green,
Yellow, Light Blue, Pink, Light Cyan

#### Currently Supported Background Colors
Black, Red, Green, Blue, Orange, Purple, Cyan, Light Gray

#### Currently Supported Text Formats
Bold, Disable, Underline, Blink (depends on OS and terminal), Reverse, Strike Through, Concealed

#### Currently Supported Log Types
Info (Information), Error (Error), Warn (Warning), Hint (Hint), Debug (Debug)

#### Usage Example
```python
from __future__ import print_function
from xtermcolors import *
print(value1, value2, sep='-', end='\n', file=sys.stdout, color='red', bg_color='orange', text_format='bold', log_type='info')

```