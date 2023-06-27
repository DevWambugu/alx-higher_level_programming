#!/usr/bin/python3
# 2-square.py
# DevWambugu
"""Define a class Square."""


class Square:
    '''Define a class Square'''
    def __init__(self, size=0):
        """Instantiation with optional size.
        size must be an integer, otherwise raise a TypeError
        exception with the message 'size must be an integer'.
        If size is less than 0, raise a ValueError exception
        with the message 'size must be >= 0'.

        Args:
            size (int): The type and value of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
