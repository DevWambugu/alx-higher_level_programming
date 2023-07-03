#!/usr/bin/python3
# 2-rectangle.py
# DevWambugu
"""Define a class Rectangle."""


class Rectangle:
    '''Define a class Rectangle.'''
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        '''Instantiation with optional width and height.'''
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def static_method():
        '''This is a static method.'''
        return "This is a static method."

    def bigger_or_equal(rect_1, rect_2):
        '''Returns the biggest rectangle based on the area'''
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.width * rect_1.height >= rect_2.width * rect_2.height:
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        '''Returns a new Rectangle instance with width == height == size'''
        return cls(size, size)
