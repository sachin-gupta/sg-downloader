#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' This is the main file for the Project '''

''' Project Imports (Python Standard Libraries) '''
import sys, time, os, six, logging, traceback

''' Project Imports (This Project Libraries) '''

''' External Imports (3rd Party Libraries) '''

''' ----------------- Main() ----------------- '''
def HelloWorld():
    print('\r\nHello World')

    raise Exception("Test Exception in Hello World")

''' ----------------- Main() ----------------- '''
def main():
    """
    This is the main function of the project
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
    