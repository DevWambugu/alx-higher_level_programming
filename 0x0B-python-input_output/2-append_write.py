#!/usr/bin/python3
#  2-append_write.py
#  DevWambugu
'''Thi function adds a string at the end of 
text and returns number of character written'''


def append_write(filename="", text=""):
    '''This function appends a string
    at the end of a text and returns no of characters'''
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
