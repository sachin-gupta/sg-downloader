#!/usr/bin/env python
# -*- coding: utf-8 -*-

from . import helpers

def get_hmm():
    """Get a thought from utils."""
    return 'Get a hmm from utils.'

def hmm():
    """Utils Contemplation..."""
    if helpers.get_answer():
        print(get_hmm())

def add(a, b):
    """
    Simple method for sphinx document generator. This method adds two numbers

    :type a: integer
    :param a: first number to be added

    :type b: integer
    :param b: second number to be added
    """
    c = a+b
    return c
