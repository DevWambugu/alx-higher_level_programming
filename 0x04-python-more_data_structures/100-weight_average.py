#!/usr/bin/python3

#   return the weighted average of all integers tuple
def weight_average(my_list=[]):
    '''Returns the weighted average of all integer tuples.'''
    if len(my_list) == 0:
        return 0
    tple_result = 0
    weight_sum = 0

    for i in range(len(my_list)):
        tple = my_list[i]
        value_1 = tple[0]
        value_2 = tple[1]
        tple_result += value_1 * value_2
        weight_sum += value_2
    return tple_result / weight_sum
