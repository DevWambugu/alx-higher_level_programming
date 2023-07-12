#!/usr/bin/python3
#  100-my_int.py
#  DevWambugu
'''this class MYint inherits from int'''


class MyInt(int):
    '''my class that inherits from the class int'''
    def __eq__(self, other):
        '''This function overrides the equals
        method'''
        return not super().__eq__(other)

    def __ne__(self, other):
        '''This function overides the not equals
        method'''
        return super().__eq__(other)
