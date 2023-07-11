#!/usr/bin/python3
#  6-load_from_json_file.py
#  DevWambugu
'''create an object from a json file'''
import json


def load_from_json_file(filename):
    '''This function creates an object
    from a json file'''
    with open(filename) as f:
        return json.load(f)
