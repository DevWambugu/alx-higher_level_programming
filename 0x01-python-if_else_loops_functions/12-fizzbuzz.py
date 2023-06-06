#!/usr/bin/python3

#  prints the numbers from 1 to 100 separated by a space
def fizzbuzz():
    '''print numbers. replace with fizz, fizzbuzz or buzz'''
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("{} ".format("FizzBuzz"), end="")
        elif i % 3 == 0:
            print("{} ".format("Fizz"), end="")
        elif i % 5 == 0:
            print("{} ".format("Buzz"), end="")
        else:
            print("{} ".format(i), end="")
