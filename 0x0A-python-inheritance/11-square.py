#!/usr/bin/python3
#  9-rectangle.py
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
        if value < 1:
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

    def area(self):
        '''this function returns
        the area of the rectangle'''
        return self.__width * self.__height

    def __str__(self):
        '''this function returns the
        rectangle description'''
        return f"[Rectangle] {self.__width}/{self.__height}"

    def __repr__(self):
        '''this function returns
        str'''
        return str(self)


class Square(Rectangle):
    '''Inherits from Rectangle'''

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        '''returns square description'''
        return f"[Square] {self.__size}/{self.__size}"

    def __repr__(self):
        '''returns str'''
        return str(self)
