#!/usr/bin/python3
# 3-is_kind_of_class.py
# DevWambugu
"""if the object is an instance of a class
   that inherited from, the specified class
"""


def is_kind_of_class(obj, a_class):
    '''this function checks if an object
    is an insatnce of a clas from which 
    it is inherited from
    '''
    return isinstance(obj, a_class)

