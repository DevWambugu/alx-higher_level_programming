#!/usr/bin/python3
'''
This script finds a peak in a list of unsorted integers
'''


def find_peak(list_of_integers):
    '''find the peak in a list of integers'''
    if len(list_of_integers) < 3:
        return None
    
    for list_index in range(1, len(list_of_integers) - 1):
        if list_of_integers[list_index] == list_of_integers[list_index - 1] and list_of_integers[list_index] == list_of_integers[list_index + 1]:
            return list_of_integers[list_index]
        elif list_of_integers[list_index] > list_of_integers[list_index - 1] and list_of_integers[list_index] > list_of_integers[list_index + 1]:
            return list_of_integers[list_index]
