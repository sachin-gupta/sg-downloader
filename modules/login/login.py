#!/usr/bin/env python
# -*- coding: utf-8 -*-

from . import helpers

def get_hmm():
    """Get a thought from login."""
    return 'Get a hmm from login.'

def hmm():
    """Login Contemplation..."""
    if helpers.get_answer():
        print(get_hmm())