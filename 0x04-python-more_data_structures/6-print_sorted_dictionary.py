#!/usr/bin/python3

#  print a dictionary by ordered keys
def print_sorted_dictionary(a_dictionary):
    '''prints a dictionary by ordered keys'''
    sorted_keys = sorted(a_dictionary.keys())
    for i in sorted_keys:
        print(i, ":", a_dictionary[i])
