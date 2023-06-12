#!/usr/bin/python3

#  delete an item at a specif location
def delete_at(my_list=[], idx=0):
    '''deletes an item at a specific index'''
    if idx < 0 or idx > len(my_list):
        return my_list
    del my_list[idx]
    return my_list
