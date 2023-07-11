#!/usr/bin/python3
# 1-write_file.py
# DevWambugu
'''function writes a string to a text file (UTF8)
and returns the number of characters written
'''


def write_file(filename="", text=""):
    '''this function write a string to a textfile
    and returns number of characters written'''
    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(text)
