#!/usr/bin/python3
#  3-to_json_string.py
#  DevWambugu
'''return the json representation
of a string'''
import json


def to_json_string(my_obj):
    '''returns the json representation
    of a string'''
    return json.dumps(my_obj)
