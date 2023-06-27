#!/usr/bin/python3

#  print the first x elements of a list and only integers
def safe_print_list_integers(my_list=[], x=0):
    '''prints the first x elements of a list and only integers'''
    count = 0
    for i in range(x):
        try:
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                count += 1
        except (ValueError, IndexError):
            continue
    print()
    return count
