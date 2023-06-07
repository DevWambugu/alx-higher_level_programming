#!/usr/bin/python3

# Print string in uppercase
def uppercase(str):
    '''Prints a string in uppercase followed by a new line'''
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            A_letter = ord(i) - 32
            i = chr(A_letter)
        print("{}".format(i), end="")
    print("")
