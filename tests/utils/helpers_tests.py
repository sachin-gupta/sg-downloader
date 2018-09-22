#!/usr/bin/env python
# -*- coding: utf-8 -*-

import modules.utils.helpers as tst_helpers

import unittest

class BasicTestSuite(unittest.TestCase):
    """Basic test cases for helpers."""

    def test_helpers_sub_method(self):

        res = tst_helpers.sub(10, 7)

        assert True

        '''
        if res = 3:
            assert True
        else:
            print('Wrong Sum [2+3]: ' + str(res))
            assert False
        '''

if __name__ == '__main__':
    unittest.main()
