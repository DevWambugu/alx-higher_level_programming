#!/usr/bin/python3
#  DevWambugu
#  101-locked_class.py
'''Create a class called LockedClass'''


class LockedClass:
    '''This class prevents a user creating
    an instance except one called 
    first_name'''
    __slots__ = ('first_name',)

    def __setattr__(self, name, value):
        '''create a function that
	raises an attribute error
	when a user tries to create another class
	'''
        if not hasattr(self, 'first_name') and name != 'first_name':
            raise AttributeError(f"[AttributeError] 'LockedClass' object has no attribute '{name}'")
        super().__setattr__(name, value)
