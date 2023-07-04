#!/usr/bin/python3
#  2-matrix_divided.py
#  DevWambugu
'''function divides all elements of a matrix'''


def matrix_divided(matrix, div):
    '''this function divides all elements
    in amatrix. matrix must be a
    list of lists of integers or floats
    Each row of the matrix must be of the same size
    div must be a number (integer or float)
    div can’t be equal to 0
    All elements of the matrix should be divided
    by div, rounded to 2 decimal places
    Returns a new matrix
    '''
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for inner_list in matrix:
        if not isinstance(inner_list, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        
        for element in inner_list:
            if not (isinstance(element, int) or isinstance(element, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
    
    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")
    
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            new_element = round(element / div, 2)
            new_row.append(new_element)
        new_matrix.append(new_row)
    
    return new_matrix
