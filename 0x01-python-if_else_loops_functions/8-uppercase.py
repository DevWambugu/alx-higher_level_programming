#!/usr/bin/python3

# Print string in uppercase
def uppercase(str):
    '''Prints a string in uppercase followed by a new line'''
    for i in str:
        if ord(i) >= 97:
            A_letter = ord(i) - 32
            letter = chr(A_letter)
            print("{}".format(letter), end="")
