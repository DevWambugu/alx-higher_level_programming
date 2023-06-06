#!/usr/bin/python3

#  print letters in reverse order.
#  alternate caps and small
#  start with small z
for i in range(122, 96, -1):
    if i % 2 == 0:
        letter = chr(i)
    else:
        letter = chr(i - 32)
    print("{}".format(letter), end="")
