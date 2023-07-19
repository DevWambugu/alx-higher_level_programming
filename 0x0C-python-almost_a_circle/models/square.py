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
        def __init__(self, *args, **kwargs):
            if len(args) > 0:
                if args[0] is not None:
                    self.id = args[0]
                if len(args) > 1:
                    self.size = args[1]
                if len(args) > 2:
                    self.x = args[2]
                if len(args) > 3:
                    self.y = args[3]
            else:
                if 'id' in kwargs and kwargs['id'] is not None:
                    self.id = kwargs['id']
                if 'size' in kwargs:
                    self.size = kwargs['size']
                if 'x' in kwargs:
                    self.x = kwargs['x']
                if 'y' in kwargs:
                    self.y = kwargs['y']

    def to_dictionary(self):
        '''returns the dictionary representation of a Square'''
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
