#!/usr/bin/python3
#  8-class_to_json.py
#  DevWambugu
''' returns the dictionary description
with simple data structure
(list, dictionary, string, integer and boolean)
for JSON serialization of an object
'''


def class_to_json(obj):
    '''this function takes an object obj
    and returns a dictionary description
    with a simple data structure'''
    return obj.__dict__
