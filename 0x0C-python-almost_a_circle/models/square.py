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
