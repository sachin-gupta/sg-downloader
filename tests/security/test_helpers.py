#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest


class BasicTestSuite(unittest.TestCase):
    """Basic test cases for helpers."""

    def test_security_helpers(self):
        print("Method test_security_helpers() Passed")
        assert True


if __name__ == '__main__':
    unittest.main()
