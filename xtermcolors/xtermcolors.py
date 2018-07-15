#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
xtermcolors - Smart custom print function with color and log information support.
Available in python 2.7.x

:copyright: 2018 Dalwar Hossain
:Licence: MIT

This module uses print_function from __futute__ import with additional
parameters

To know more about __future__.print_function please visit
https://docs.python.org/2/library/__future__.html

Currently Supported Foreground Colors:
======================================
Black, Red, Green, Orange, Blue,Purple, Cyan, Light Gray, Dark Gray, Light Red, Light green,
Yellow, Light Blue, Pink, Light Cyan

Currently Supported Background Colors:
======================================
Black, Red, Green, Blue, Orange, Purple, Cyan, Light Gray

Currently Supported Text Formats:
=================================
Bold, Disable, Underline, Blink, Reverse, Strike Through, Concealed

Currently Supported Log Types:
==============================
Info (Information), Error (Error), Warn (Warning), Hint (Hint), Debug (Debug)

Usage Example:
==============
print(value1, value2, sep='', end='\n', file=sys.stdout, color=None, bg_color=None, text_format=None, log_type=None)
"""

from __future__ import print_function


# Import python libraries
import sys
if sys.version_info[0] ==2:
    import __builtin__
if sys.version_info[0] == 3:
    import builtins as ____builtin__


# Source code meta data
__author__ = 'Dalwar Hossain'
__email__ = 'dalwar.hossain@protonmail.com'
__description__ = 'Python module to print colorful text and log information'
__url__ = ''
__copyright__ = '(c) 2018 %s' % __author__
__license__ = 'MIT'
__version__ = '1.0'


# Python package import
__all__ = ['print']


# Define Foreground Colors
foreground_colors = {
    'black': 30, 'red': 31, 'green': 32,
    'orange': 33, 'blue': 34, 'purple': 35,
    'cyan': 36, 'light_gray': 37, 'dark_gray': 90,
    'light_red': 91, 'light_green': 92, 'yellow': 93,
    'light_blue': 94, 'pink': 95, 'light_cyan': 96
}

# Define Background Colors
background_colors = {
    'black': 40, 'red': 41, 'green': 42,
    'orange': 43, 'blue': 44, 'purple': 45,
    'cyan': 46, 'light_gray': 47
}

# Define Text Formats
text_formats = {
    'bold': 1, 'dark': 2, 'underline': 4,
    'blink': 5, 'reverse': 7, 'concealed': 8,
    'strike_through': 9
}

# Define valid log type
log_types = {
    'info': 'pink', 'error': 'red',
    'warn': 'orange', 'hint': 'blue',
    'debug': 'dark_gray'
}


# Custom print function with a few extra keywords
def print(*args, **kwargs):
    """
    Normally print function in python prints values to a stream / stdout
    >> print(value1, value2, sep='', end='\n', file=sys.stdout)

    Current package usage:
    ======================
    print(value1, value2, sep='', end='\n', file=sys.stdout, color=None,
    bg_color=None, text_format=None, log_type=None)

    :param args: Values (str) to print
    :param kwargs: Text formats like sep, end, color, background, text format, log type (ERROR, INFO, WARNING, DEBUG)
    :return: Colored text to stdout (Console)
    """

    # Pop out color and background values from kwargs
    color_name = kwargs.pop('color', None)
    bg_color = kwargs.pop('bg_color', None)
    log_type = kwargs.pop('log_type', None)

    # Check formats, create a list of text formats
    txt_formats = kwargs.pop('text_format', [])
    if sys.version_info[0] == 2:
        str_type = basestring
    elif sys.version_info[0] == 3:
        str_type = str
    else:
        str_type = basestring
    if isinstance(txt_formats, str_type):
        txt_formats = [txt_formats]

    # Check for file keyword
    file_name = kwargs.get('file', sys.stdout)

    # Check for foreground and background colors
    if color_name or bg_color or log_type:
        # Pop out the 'end' argument
        end_ = kwargs.pop('end', "\n")
        kwargs['end'] = ""

        # If log type argument is provided
        if log_type:
            if log_type not in log_types.keys():
                print('Log type not valid!', log_type='error')
                sys.exit(1)
            if log_type == 'info':
                __builtin__.print('\033[{}m[INF] '.format(foreground_colors[log_types[log_type]]), file=file_name, end='')
                __builtin__.print('\033[0m', file=file_name, end='')
            if log_type == 'warn':
                __builtin__.print('\033[{}m[WRN] '.format(foreground_colors[log_types[log_type]]), file=file_name, end='')
                __builtin__.print('\033[0m', file=file_name, end='')
            if log_type == 'error':
                __builtin__.print('\033[{}m[ERR] '.format(foreground_colors[log_types[log_type]]), file=file_name, end='')
                __builtin__.print('\033[0m', file=file_name, end='')
            if log_type == 'hint':
                __builtin__.print('\033[{}m[HNT] '.format(foreground_colors[log_types[log_type]]), file=file_name, end='')
                __builtin__.print('\033[0m', file=file_name, end='')
            if log_type == 'debug':
                __builtin__.print('\033[{}m[DBG] '.format(foreground_colors[log_types[log_type]]), file=file_name, end='')
                __builtin__.print('\033[0m', file=file_name, end='')

        # If foreground color argument is provided
        if color_name:
            if color_name not in foreground_colors.keys():
                print('Invalid color code!', log_type='error')
                sys.exit(1)
            __builtin__.print('\033[{}m'.format(foreground_colors[color_name]), file=file_name, end='')

        # If background color argument is provided
        if bg_color:
            if bg_color not in background_colors.keys():
                print('Invalid background color code!', log_type='error')
                sys.exit(1)
            __builtin__.print('\033[{}m'.format(background_colors[bg_color]), file=file_name, end='')

        # If text formats are provided
        for txt_format in txt_formats:
            __builtin__.print('\033[{}m'.format(text_formats[txt_format]), file=file_name, end='')
        # Print values
        __builtin__.print(*args, **kwargs)
        # Reset
        __builtin__.print('\033[0m',  file=file_name, end=end_)
    else:
        __builtin__.print(*args, **kwargs)


# main function
def main():
    print('This is a normal string!')
    print('This is a black string', 'with light gray background and underline',
          color='black', bg_color='light_gray', text_format='underline', end='', sep=', ')
    print('!!!!!', color='red', text_format=['bold', 'blink'])
    print('This line shows a hint message on the screen!', log_type='hint')
    print('This message shows a general information on the screen!', log_type='info')
    print('This is an ERROR message!', color='red', log_type='error')
    print('This message shows a warning to the user!', log_type='warn')
    print('This message is a debug message!', log_type='debug')
    # Rainbow message!!
    print('This ', color='red', end='')
    print('is ', color='orange', end='')
    print('a ', color='yellow', end='')
    print('rainbow ', color='green', end='')
    print('colored ', color='cyan', end='')
    print('string ', color='blue', end='')
    print('message!', color='purple')


# Standard boilerplate for running the source code
if __name__ == '__main__':
    main()
