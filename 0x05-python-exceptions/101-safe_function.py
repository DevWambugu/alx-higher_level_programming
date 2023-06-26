#!/usr/bin/python3
import sys

#  executes a function safely


def safe_function(fct, *args):
    '''executes a function safely
    fct will be always a pointer to a function
    Returns the result of the function'''
    try:
        result = fct(*args)
    except Exception as e:
        print("Exception:", e, file=sys.stderr)
        result = None
    return result
