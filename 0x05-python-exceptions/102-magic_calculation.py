#!/usr/bin/python3

#  does magical calculations
def magic_calculation(a, b):
    '''returns (a / b) ** i'''
    rst = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            rst += a ** b / i
        except:
            rst += a + b
    return rst
