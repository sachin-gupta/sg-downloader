#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Format: from <package [or folder]>(1..inf) import <module or class (.py file)>
- Thus from source package (or folder) import runner (module or .py file)
  and then call main() method of imported module

- No exception handling or CTRL-C handling in main.py (client code to source module).
It's inside runner.main()

- Loading runner.py module from source sub-package with current file
'''
from source import runner

runner.main()
