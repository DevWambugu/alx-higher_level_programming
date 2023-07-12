#!/usr/bin/python3
#   101-add_attribute.py
#   DevWambugu
'''Write a function that adds a new attribute
to an object if it’s possible'''


def add_attribute(obj, attr_name, attr_value):
    '''adds a new attribute. if not possible
    it raises a type error'''
    if hasattr(obj, attr_name):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attr_name, attr_value)
