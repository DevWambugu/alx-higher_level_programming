#!/usr/bin/python3
#  7-add_item.py
#  DevWambugu
'''adds all arguments to a python list
then saves them to a file'''
import sys


if __name__ == "__main__":
    '''specifys that the block of code will
    run when executed directly not
    when imported'''
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        items_loaded = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = []
    items.extend(sys.argv[1:])
    save_to_json_file(items, "add_item.json")
