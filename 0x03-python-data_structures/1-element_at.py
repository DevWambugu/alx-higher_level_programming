#!/usr/bin/python3

#  retrieve an element from a list like c
def element_at(my_list, idx):
    '''retrieves an element from a list like c'''
    if idx < 0:
        return None
    elif idx > (len(my_list) - 1):
        return None
    else:
        return (my_list[idx])
