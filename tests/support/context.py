#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

"""
If we run pytest, it'll start in tests/support folder where `import src` will not work as src module is not found.
This context file will import it for test
"""

# Get root path of workspace and add it to Python module search path
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../..')))

# Import src modules into context.py module
from src.support import helpers
from src.support import utilities
