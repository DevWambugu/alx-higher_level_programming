#!/usr/bin/python3

#  return a set of common elements in two sets
def common_elements(set_1, set_2):
    '''returns a set of common elements in two sets'''
    common_elements = set(filter(lambda x: x in set_2, set_1))
    return common_elements
