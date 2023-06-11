#!/usr/bin/python3

# replaces an element in a list at a specific position
# without modifying the original list (like in C)
def new_in_list(my_list, idx, element):
    '''replaces an element in a list'''
    new_list = my_list[:]
    if idx < 0:
        return new_list
    elif idx > (len(my_list) - 1):
        return new_list
    else:
        new_list[idx] = element
        return new_list
