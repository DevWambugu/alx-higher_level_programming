#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer


class max_integer_test(unittest.TestCase):
    
    def max_integer(self):
        '''Searches for max int in  an ordered list'''
        lst = [1, 3, 5, 2, 4]
        self.assertEqual(max_integer(ordered), 5)
if __name__ == '__main__':
    unittest.main()
