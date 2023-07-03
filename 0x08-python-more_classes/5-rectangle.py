#!/usr/bin/python3
# 2-rectangle.py
# DevWambugu
"""Define a class Rectangle."""


class Rectangle:
    '''Define a class Rectangle.'''
    def __init__(self, width=0, height=0):
        '''Instantiation with optional width and height.'''
        self.__width = width
        self.__height = height

    @property
    def width(self):
        '''Property to retrieve width.'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Sets the width value.'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''Retrieves the property.'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Sets the height value.'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''Returns the area'''
        return self.height * self.width

    def perimeter(self):
        '''Returns the perimeter'''
        if self.width == 0 or self.height == 0:
            perimeter = 0
            return perimeter
        else:
            perimeter = (2 * self.width) + (2 * self.height)
            return perimeter
    
    def __str__(self):
        '''Returns a string representation of the rectangle'''
        if self.width == 0 or self.height == 0:
            return ""
        else:
            return "\n".join(["#" * self.width] * self.height)

    def __repr__(self):
        '''Returns a string representation that can recreate the object'''
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        '''Prints "Bye rectangle..." when an instance is deleted'''
        print("Bye rectangle...")
