#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 23 Sep 2018
@author: Sachin Gupta
"""

''' Use helpers module from same (.) package. Renamed as mod_helpers for code safety.'''
from . import helpers as mod_helpers

def get_hmm():
    """Get a hmm() from sub-package login."""
    return 'Get a hmm() from sub-package login.'

def hmm():
    """Hmm() Method Of Login Module"""
    if mod_helpers.get_answer():
        print(get_hmm())
