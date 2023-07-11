#!/usr/bin/python3
#  4-from_json_string.py
#  DevWambugu
'''this function returns a python object'''
import json


def from_json_string(my_str):
    '''Converts the json object mystring to
    a python datastructure'''
    return json.loads(my_str)
