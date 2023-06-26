#!/usr/bin/python3

#  a function that divides 2 integers and prints the result
def safe_print_division(a, b):
    '''divides 2 integers and prints the result'''
    try:
        rslt = (a / b)
    except (TypeError, ZeroDivisionError):
        rslt = None
    finally:
        print("Inside result: {}".format(rslt))
    return rslt
