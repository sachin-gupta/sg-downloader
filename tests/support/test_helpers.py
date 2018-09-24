#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from src.support import helpers


class BasicTestSuite(unittest.TestCase):
    """Basic test cases for helpers."""

    def test_support_helpers(self):

        res = helpers.sub(10, 7)

        if res == 3:
            print('~~~ Right Subtraction [10-7]: ' + str(res))
            assert True
        else:
            print('~~~ Wrong Subtraction [10-7]: ' + str(res))
            assert False


if __name__ == '__main__':
    unittest.main()
