#!/usr/bin/python3
#  5-text_indentation.py
#  DevWambugu
'''prints a text with 2 new lines after each
of these characters: ., ? and
'''


def text_indentation(text):
    '''prints a text with 2 new lines after each
    of these characters: ., ? and
    There should be no space at the beginning or
    at the end of each printed line
    text must be a string, otherwise raise a TypeError
    exception with the message text must be a string
    '''
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuations = [".", "?", ":"]
    rlt = ""
    for c in text:
        rlt += c
        if c in punctuations:
            rlt += "\n\n"

    print(rlt.strip(), end="")
