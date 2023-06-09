#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer


class max_integer_test(unittest.TestCase):
    
    def test_max_integer(self):
        '''Returns the max in an unordered list'''
        lst = [1, 3, 5, 2, 4]
        self.assertEqual(max_integer(lst), 5)

    def test_max_integer_ordered(self):
        '''Ordered list'''
        lst = [1, 2, 3, 4, 5]
        self.assertEqual(max_integer(lst), 5)

    def test_max_integer_with_negative(self):
        '''With a negative value'''
        lst = [1, 2, -5, 4, 5]
        self.assertEqual(max_integer(lst), 5)

if __name__ == '__main__':
    unittest.main()
