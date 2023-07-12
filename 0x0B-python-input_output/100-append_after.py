#!/usr/bin/python3
#  100-append_after.py
#  DevWambugu
'''This function inserts a string
after a specific string'''


def append_after(filename="", search_string="", new_string=""):
    '''This function takes 3 arguments. With the file open,
    search the string and insert the new string'''
    with open(filename, "r") as f:
        '''use the readlines functions to read strings
        in the file and store them in the strings variable
        '''
        strings = f.readlines()

    with open(filename, "w") as f:
        '''open the file in write mode.
        iterarte over the lines and write each to thefile.
        use the .write() function.
        as you loop, if the search string is found
        write it and move to the next line.'''
        for i in strings:
            f.write(i)
            if search_string in i:
                f.write(new_string)
