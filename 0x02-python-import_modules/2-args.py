#!/usr/bin/python3

if __name__ == "__main__":
    '''prints the number of and the list of its arguments'''

    import sys

    # get total arguments
    args = len(sys.argv)
    # print number of arguments and the args
    if args == 2:
        print("{} argument:".format(args - 1))
        print("1: {}".format(sys.argv[1]))
    elif args == 1:
        print("{} arguments.".format(0))
    else:
        print("{} arguments:".format(args - 1))
        for i in range(1, args):
            print("{}: {}".format(i, sys.argv[i]))
