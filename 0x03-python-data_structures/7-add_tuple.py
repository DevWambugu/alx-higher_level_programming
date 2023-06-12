#!/usr/bin/python3

#  add two tuples
def add_tuple(tuple_a=(), tuple_b=()):
    '''tis function adds 2 tuples'''
    if len(tuple_b) >= 2:
        return tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
    elif len(tuple_b) == 1:
        return tuple_a[0] + tuple_b[0], tuple_a[1]
    else:
        return tuple_a
