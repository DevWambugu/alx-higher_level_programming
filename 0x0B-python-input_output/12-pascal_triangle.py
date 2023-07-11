#!/usr/bin/python3
#  12-pascal_triangle.py
#  DevWambugu
'''ctreate a function that returns a list of lists
of integers representing the Pascal’s triangle
'''


def pascal_triangle(n):
    '''This function retuns a list of lists
    of integers representing the Pascal’s triangle
    '''
    elements_list = []
    if n <= 0:
        return elements_list
    #  initialize pascal's triangle with the first
    #  row which only contains one
    pascal_triangle = [[1]]
    #  To represent each row
    #  We iterate from i = 1 to n-1
    for i in range(1, n):
        #  we initialize each row with 1 before starting
        pascal_row = [1]
        prev_row = pascal_triangle[i - 1]
        for j in range(1, i):
            '''iterate from j = 1 to i-1
            calculate values by summing the corresponding
            elements from the previous row and append them to
            to the next row. Add a 1 at the end of each row'''
            pascal_row.append(prev_row[j - 1] + prev_row[j])
        #  append each row and return the triangle list
        pascal_row.append(1)
        pascal_triangle.append(pascal_row)
    return pascal_triangle
