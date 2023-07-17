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
        instance with the character #
        It also instance with the character #
        by taking care of x and y'''
        for i in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        '''this function overides the
        str method and return a custom
        string'''
        return f"[Rectangle]({self.id})"\
               f"{self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args):
        '''assigns an argument to every attribute
        Note that argument order is important when kwargs is
        not included. Else if you include kwargs,
        argument order is not important. kwargs contains
        key and value pairs. If args exists, do not move to kwargs
        '''
        number_of_args = len(args)
        if args:
            if number_of_args >= 1:
                self.id = args[0]
            if number_of_args >= 2:
                self.width = args[1]
            if number_of_args >= 3:
                self.height = args[2]
            if number_of_args >= 4:
                self.x = args[3]
            if number_of_args >= 5:
                self.y = args[4]
        elif kwargs:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'width':
                    self.width = value
                elif key == 'height':
                    self.height = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

    def to_dictionary(self):
        '''this function returns the
        dictioanry representation of a triangle'''
        return 
        {
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
