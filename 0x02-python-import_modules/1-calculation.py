#!/usr/bin/python3
#  import functions from the file calculator_1.py
#  do some Maths, and prints the result

if __name__ == "__main__":
    '''does some math and prints the result'''
    from calculator_1 import add, mul, sub, div

    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
