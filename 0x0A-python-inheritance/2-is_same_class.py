#!/usr/bin/python3
# 2-is_same_class.py
# DevWambugu
"""checks whther the instance is same as the object."""


def is_same_class(obj, a_class):
    '''this function checks if
    the arguments are the same. That is
    if the instance is same as object
    '''
    return type(obj) is a_class
