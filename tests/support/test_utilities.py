#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

#from src.support import utilities
from .context import utilities as utilities


class AdvancedTestSuite(unittest.TestCase):
    """Basic test cases for utils."""

    def test_support_utilities(self):

        res = utilities.add(2, 3)

        if res == 5:
            print('~~~ Right Addition [2+3]: ' + str(res))
            assert True
        else:
            print('~~~ Wrong Addition [2+3]: ' + str(res))
            assert True


if __name__ == '__main__':
    unittest.main()
