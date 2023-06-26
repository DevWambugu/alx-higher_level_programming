#!/usr/bin/python3

# Write a function that prints x elements of a list
def safe_print_list(my_list=[], x=0):
    '''prints x elements in a list'''
    j = 0
    for i in range(x):
        try:
            print(my_list[i], end=" ")
            j += 1
        except IndexError:
            pass
    print()  # Print a new line after the elements
    return j
