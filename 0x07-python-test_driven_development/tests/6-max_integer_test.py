#!/usr/bin/python3
import unittest
import 6-max_integer.py


class max_integer_test(unittest.TestCase):
    
    def max_integer(self):
        lst = [1, 3, 5, 2, 4]
        expected_max = 5
        max_val = max(lst)

        self.assertEqual(max_val, expected_max, f"Expected max: {expected_max}, Actual max: {max_val}")
if __name__ == '__main__':
    unittest.main()
