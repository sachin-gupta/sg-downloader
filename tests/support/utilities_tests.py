#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from source.support import utilities

class AdvancedTestSuite(unittest.TestCase):
    """Basic test cases for utils."""

    def test_utils_add_method(self):

        res = utilities.add(2, 3)

        if res==5:
            print('~~~ Right Addition [2+3]: ' + str(res))
            assert True
        else:
            print('~~~ Wrong Addition [2+3]: ' + str(res))
            assert False


if __name__ == '__main__':
    unittest.main()
