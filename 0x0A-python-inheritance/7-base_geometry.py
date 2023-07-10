#!/usr/bin/python3
#  7-base_geometry.py
#  DevWambugu
"""improve the class to raise an exception error
it also validates a value
"""


class BaseGeometry:
    '''This class contains a function that raises an exception error
    and validates as value by creating an instance'''
    def area(self):
        '''this function raises an exception error'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''validates a value
        assume that the value is always a string
        '''
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value < 1:
            raise ValueError(f"{name} must be greater than 0")
