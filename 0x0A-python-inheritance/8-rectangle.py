#!/usr/bin/python3
#  8-rectangle.py
#  DevWambugu
"""improve the class to raise an exception error
it also validates a value
containsa class that inherits from BaseGeometry
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
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    '''This class inherits from base geometry'''

    def __init__(self, width, height):
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
