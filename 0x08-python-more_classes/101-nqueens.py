#!/usr/bin/python3
#  101-nqueens.py
#  DevWambugu
import sys
'''create a program that solves the queens puzzle'''


def solve_nqueens(n):
    '''this function give the solution for n
    queens. It starts by checking if n is an integer
    value and is more than 4. If not it prints a message
    and exits with a value 1 indicating that 
    there is an error
    '''
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    def is_safe(board, row, col):
        '''This functon checks whether ity is safe to place
	a queen at a given position on a chess board
	if safe it returns true. False otherwise
	'''
        for i in range(row):
            if board[i] == col or board[i] - col == i - row or board[i] - col == row - i:
                return False
        return True

    def solve_util(board, row):
        '''This function takes in 2 arguments. Board and row
	if row is equal to value n then all quenns have been
	placed it stores the solution.
	'''
        if row == n:
            solutions.append(board.copy())
            return

        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                solve_util(board, row + 1)
                board[row] = -1

    '''Initialize the chessboard starting at element
    [-] n times. Initailize an empty lists to store sltns
    call the solve util function to check whether
    queens have been placed
    '''
    board = [-1] * n
    solutions = []
    solve_util(board, 0)

    '''Print the solutions in the desired format
    by printing the solutions placed in the
    solutions list
    '''
    for solution in solutions:
        formatted_solution = [[i, solution[i]] for i in range(n)]
        print(formatted_solution)

'''check the number of arguments
if number of correct args is not given
print a message and exit with one to indicate error.
Other wise call the solve queens function and raise a value error
if N is not a number
'''
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    n = int(sys.argv[1])
    solve_nqueens(n)
except ValueError:
    print("N must be a number")
    sys.exit(1)
