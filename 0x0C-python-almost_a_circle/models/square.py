#!/usr/bin/python3
#  base.py
#  DevWambugu
'''The square class inherits
from the rectangle class
'''
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    '''This class inherits from the rectangle class
    this makes sense because a square is a special
    rectangle'''

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        '''get the size of the square'''
        return self.width

    @size.setter
    def size(self, value):
        '''sets the attributes'''
        self.width = value
        self.height = value

    def __str__(self):
        '''this function overides the
        str method and return a custom
        string'''
        return f"[Rectangle]({self.id})"\
               f"{self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        '''this public method
        assigns attributes'''
        if len(args) != 0:
            argument = 0
            for i in args:
                if argument == 0:
                    if argument is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = i
                elif argument == 1:
                    self.size = i
                elif argument == 2:
                    self.x = i
                elif argument == 3:
                    self.y = i
                argument += 1

        elif len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
