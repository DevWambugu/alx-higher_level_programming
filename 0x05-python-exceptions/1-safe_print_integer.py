#!/usr/bin/python3

#  print an integer with "{:d}".format()
def safe_print_integer(value):
    '''prints an integer with "{:d}".format()'''
    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        return False
