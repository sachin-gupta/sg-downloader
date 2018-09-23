#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 23 Sep 2018
@author: Sachin Gupta
"""

from . import helpers

import random

def get_hmm():
    """Get a thought from utils."""
    return 'Get a hmm from utils.'

def hmm():
    """Utils Contemplation..."""
    if helpers.get_answer():
        print(get_hmm())

def add(a, b):
    """
    Simple method for sphinx document generator. This method adds two numbers or
    just returns a random value

    :type a: integer
    :param a: first number to be added

    :type b: integer
    :param b: second number to be added
    """
    flag = random.random()

    if flag < 0.5:
        c = a+b
    else:
        c = flag

    return c
