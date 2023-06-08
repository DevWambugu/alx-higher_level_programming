#!/usr/bin/python3
#  import the function def add(a, b): from the file add_0.py
#  print the result of the addition 1 + 2 = 3
if __name__ == "__main__":
    '''prints the sum of 2 integers'''
    from add_0 import add

    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
