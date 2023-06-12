#!/usr/bin/python3

#  return a tuple with the length of a string
#  and its first character
def multiple_returns(sentence):
    '''returns a tuple with the length of a string
    and its first character'''
    length = len(sentence)
    if length == 0:
        first = None
    else:
        first = sentence[0]
    return (length, first)
