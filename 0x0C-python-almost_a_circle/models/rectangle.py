#!/usr/bin/python3
#  base.py
#  DevWambugu
'''This class is be the “base” of all other classes in this project.
   The goal of it is to manage id attribute in all your future classes
   and to avoid duplicating the same code (by extension, same bugs)
'''
from models.base import Base


class Rectangle(Base):
    '''This class inherits from the Base class
    It sets Private instance attributes,
    each with its own public getter and setter
    start by calling the super class
    '''
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''retrive width property as a private
        attribute'''
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        '''retrieve height property as a private
        attribute'''
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        '''retrieves x property as a
        private attribute'''
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        '''retrieves y attribue a s a private attribute'''
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__y = value

    def area(self):
        '''returns the area of the rectangle'''
        return self.__width * self.__height

    def display(self):
        ''' prints in stdout the Rectangle
        instance with the character #'''
        for i in range(self.__height):
            print("#" * self.__width)
