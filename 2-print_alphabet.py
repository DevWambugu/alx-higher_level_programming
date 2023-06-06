#!/usr/bin/python3
for i in range(26):
    lower_letter = (chr(ord('a') + i))
    if lower_letter != "q" and lower_letter != "e":
        print("{}".format(lower_letter), end="")
