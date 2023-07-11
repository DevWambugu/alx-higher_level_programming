#!/usr/bin/python3
#  5-save_to_json_file.py
#  DevWambugu
'''write an object to a textfile
using json representation'''
import json


def save_to_json_file(my_obj, filename):
    '''this fuinction takes in the arguments
    filename and python object my_obj.
    the function then writes py object
    to a file'''
    with open(filename, "w") as f:
        json.dump(my_obj, f)
