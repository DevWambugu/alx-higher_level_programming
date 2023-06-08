#!/usr/bin/python3

if __name__ == "__main__":
    """handles basic math operations"""
    from calculator_1 import add, mul, sub, div
    import sys
    # check for fundamental conditions

    args = len(sys.argv)
    if args != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    operator = sys.argv[2]
    if operator not in ['+', '-', '*', '/']:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    # get the integer values and operator

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    
    # perform the operations
    if operator == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif operator == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif operator == '*':
        print("{} * {} = {}".format(a, b, mul(a, b)))
    else:
        print("{} / {} = {}".format(a, b, div(a, b)))
