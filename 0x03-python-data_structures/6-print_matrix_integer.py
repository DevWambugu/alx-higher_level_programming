#!/usr/bin/python3

# print a matrix of integers
def print_matrix_integer(matrix=[[]]):
    '''print a matrix of integers.'''
    for r in matrix:
        for el in r:
            print("{:d}".format(el), end=" ")
        print()
