#!/usr/bin/python3
# 1-my_list.py
# DevWambugu
"""write a class that inherits from list class."""


class MyList(list):
    '''this class inherits from the class list'''
    def print_sorted(self):
        '''this function prints ints in a sorted manner'''
        sorted_list = sorted(self)
        print(sorted_list)
