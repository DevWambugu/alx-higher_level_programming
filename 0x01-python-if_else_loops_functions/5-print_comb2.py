#!/usr/bin/python3
# print numbers 0 to 99

'''Print numbers 0 to 99 separted by a comma'''
for i in range(100):
    if i < 99:
        print("{:02}, ".format(i), end="")
    else:
        print("{}".format(i))
