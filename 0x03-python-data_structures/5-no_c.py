#!/usr/bin/python3

# remove all characters c and C from a string
def no_c(my_string):
    '''removes all characters c and C from a string'''
    new_string = ""
    for i in my_string:
        if i != 'C' and i != 'c':
            new_string += i
    return new_string
