#!/usr/bin/python3
# 0-read_file.py
# DevWambugu
'''This function reads a text file and prints
it to the standard output
'''


def read_file(filename=""):
    '''Function reads a file and prints it
    to the stdout'''
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            print(line, end='')
