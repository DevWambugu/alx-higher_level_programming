#!/usr/bin/python3

#  delete a key in a dictionary
def simple_delete(a_dictionary, key=""):
    '''deletes a key in a dictionary'''
    if key in a_dictionary:
        a_dictionary.pop(key, None)
    return a_dictionary
