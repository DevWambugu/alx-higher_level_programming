#!/usr/bin/python3
#  base.py
#  DevWambugu
'''This module contains unittest cases
for the base class'''
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Base class."""

    def test_number_of__arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_for_three_bases(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_None_id(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_for_unique_id(self):
        self.assertEqual(12, Base(12).id)

    def test_the_nb_instances_after_unique_id(self):
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_public_id(self):
        b = Base(12)
        b.id = 15
        self.assertEqual(15, b.id)

    def test_nb_instances_for_private(self):
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)

    def test_string_id(self):
        self.assertEqual("hello", Base("hello").id)

    def test_float_id(self):
        self.assertEqual(5.5, Base(5.5).id)

'''run the test cases'''
if __name__ == "__main__":
    unittest.main()
