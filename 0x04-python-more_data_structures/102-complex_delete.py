#!/usr/bin/python3

#  delete keys with a specific value in a dictionary
def complex_delete(a_dictionary, value):
    '''Deletes keys with a specific value in a dictionary'''
    delete = []
    for key, val in a_dictionary.items():
        if val == value:
            delete.append(key)
    for i in delete:
        del a_dictionary[i]
    return a_dictionary
