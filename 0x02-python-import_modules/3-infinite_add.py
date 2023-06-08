#!/usr/bin/python3

if __name__ == "__main__":
    """prints the result of the addition of all arguments"""
    import sys

    args = len(sys.argv)
    total = 0
    for i in range(1, args):
        integer = int(sys.argv[i])
        total += integer
    print("{}".format(total))

