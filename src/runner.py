#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 29 July 2012
@author: Sachin Gupta
"""

''' This is the main file for the Project. It contains unhandled exception catching and CTRL-C handling '''

''' Project Imports (Python Standard Libraries) '''
import sys, time, os, six, logging, traceback

''' Project Imports (This Project Libraries) '''
''' from same package (.) and sub-package (security) import login.py module. Renamed as mod_auth for code safety. '''
from .security import login as mod_auth

''' from same package (.) and sub-package (support) import utilities.py module. Renamed as mod_utils for code safety. '''
from .support import utilities as mod_utils

''' External Imports (3rd Party Libraries) '''

''' ----------------- Main() ----------------- '''
def HelloWorld():
    # Inline Function Execution
    print('\r\nHello World - Runner.py (Main Package)')

    # Calling Sub-Package Methods
    mod_utils.hmm()
    mod_auth.hmm()

    # No more exceptions now
    # raise Exception("Test Exception in Hello World")

''' ----------------- Main() ----------------- '''
def main():
    """
    This is the main function of the PROJECT
    - It prints a message on console
    - It calls hello world which throws an exception
    """
    print('\r\n^^^ Program Started ^^^')

    HelloWorld()

if __name__ == '__main__':
    """
    This is the entry point of project
    - It calls main method and wait for exceptions
    - An exception via CTRL-C on keyboard will terminate the program
    - All other exceptions are re-raised for system to be able to handle
    """
    try:
        main()
    except KeyboardInterrupt:
        logging.warn("\r\n  CTRL-C detected, shutting down....")
        sys.exit(-1)
    except:
        logging.error("\r\n^^^ Unhandled Exception ^^^ ")
        traceback.print_exc(limit=None, file=sys.stdout)
        raise
