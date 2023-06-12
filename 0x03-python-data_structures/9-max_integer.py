#!/usr/bin/python3

# find the biggest integer in a list
def max_integer(my_list=[]):
    '''finds the largest integer'''
    if len(my_list) == 0:
        return None
    for i in range(len(my_list)):
        for j in range(0, len(my_list) - i - 1):
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    return my_list[-1]
