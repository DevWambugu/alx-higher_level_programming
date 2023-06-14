#!/usr/bin/python3

#  compute the square value of all integers of a matrix
def square_matrix_simple(matrix=[]):
    '''Computes the square value of all integers in a matrix.'''
    result = []
    for row in matrix:
        squared_row = [element ** 2 for element in row]
        result.append(squared_row)
    return result
