#!/usr/bin/python3

#  retrieve an element from a list like c
def element_at(my_list, idx):
    '''retrieves an element from a list like c'''
    if idx < 0:
        return (0)
    elif idx > len(my_list):
        return (0)
    else:
        return (my_list[idx])
