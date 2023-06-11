#!/usr/bin/python3

# prints all integers of a list, in reverse order
def print_reversed_list_integer(my_list=[]):
    '''print integers in reverse order'''
    for i in range(len(my_list)-1, -1, -1):
        print("{:d}".format(my_list[i]))
