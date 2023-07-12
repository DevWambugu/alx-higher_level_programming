#!/usr/bin/python3
# 0-lookup.py
# DevWambugu
"""Define a function that returns attributes and methods
in an object"""


def lookup(obj):
    '''returns a list of available methods and
    attributes in an object
    '''
    return dir(obj)
