#!/usr/bin/python3
# replaces an element of a list at a specific position (like in C)

def replace_in_list(my_list, idx, element):
    '''replaces an element at a specific index'''
    if idx < 0:
        return my_list
    elif idx > (len(my_list) - 1):
        return my_list
    else:
        my_list[idx] = element
        return my_list
