#!/usr/bin/env python3

# create a copy of the string
# remove the characters at a specific position
def remove_char_at(str, n):
    '''copies the string and removes a character at a specific location'''
    new_str = str[:n] + str[n+1:]
    return new_str
