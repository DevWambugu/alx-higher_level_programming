#!/usr/bin/python3

#  add all unique integers in a list
def uniq_add(my_list=[]):
    '''adds all unique integers in a list'''
    uniq_numbers = set()
    t_sum = 0
    for i in my_list:
        if i not in uniq_numbers:
            uniq_numbers.add(i)
            t_sum += i
    return t_sum
