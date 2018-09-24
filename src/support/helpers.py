#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 23 Sep 2018
@author: Sachin Gupta
"""

import random

def get_answer():
    """Get an answer from sub-package support, module helpers."""
    return True


def sub(a, b):
    """
    Simple method for sphinx document generator. This method subtract two numbers or
    just returns a random value

    :type a: integer
    :param a: first number to be subtracted

    :type b: integer
    :param b: second number to be subtracted
    """
    flag = random.random()

    if flag < 0.5:
        c = a-b
    else:
        c = flag

    return c
