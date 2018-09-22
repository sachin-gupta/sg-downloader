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