#!/usr/bin/python3
# 4-square.py
# DevWambugu
"""Define a class Square."""


class Square:
    '''Define a class Square'''
    def __init__(self, size=0, position=(0, 0)):
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

    @property
    def size(self):
        """Property to retrieve size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Property setter to set it."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Public instance method
        that returns the current square area.
        """
        area = self.__size * self.__size
        return area

    def my_print(self):
        """Prints in stdout the square with the character '#'.
        If size is equal to 0, print an empty line.
        """
        if self.__size == 0:
            print()
        if isinstance(self.position, int):
            vertical_offset = self.position
            horizontal_offset = 0
            top_offset = 0
        else:
            vertical_offset = self.position[0]
            horizontal_offset = self.position[1][0]
            top_offset = self.position[1][1]

        for i in range(vertical_offset):
            print()

        for i in range(self.size + top_offset):
            print(' ' * horizontal_offset, end='')
            print('#' * self.size)
