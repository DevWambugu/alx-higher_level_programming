#!/usr/bin/python3

# print a matrix of integers
def print_matrix_integer(matrix=[[]]):
    '''print a matrix of integers.'''
    for r in range(len(matrix)):
        for j in range(len(matrix[r])):
                print("{:d}".format(matrix[r][j]), end="")
                if j != (len(matrix[r]) - 1):
                    print(" ", end="")
        print("{}".format(""))
