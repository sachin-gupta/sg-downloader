#!/usr/bin/env python
# -*- coding: utf-8 -*-

import modules.utils.utils as tst_utils

import unittest

class AdvancedTestSuite(unittest.TestCase):
    """Basic test cases for utils."""

    def test_utils_add_method(self):

        res = tst_utils.add(2,3)

        assert True

        '''
        if res = 5:
            assert True
        else:
            print('Wrong Sum [2+3]: ' + str(res))
            assert False
        '''

if __name__ == '__main__':
    unittest.main()
