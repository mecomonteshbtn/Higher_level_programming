#!/usr/bin/python3
"""unitest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    class for testing 6-max_integer_test.py
    without arguments
    """

    def test_max_integer(self):
        """
        normal list of positive integers
        without arguments
        """
        test_list = [1, 2, 3, 8, 4]
        self.assertEqual(max_integer(test_list), 8)

    def test_max_integer_neg(self):
        """
        test case for a list of positive and negative integers
        without arguments
        """
        test_list = [1, 2, 3, 8, 4, -40, -400, -12, 0]
        self.assertEqual(max_integer(test_list), 8)

    def test_max_integer_float(self):
        """
        test case for a list of positive and negative floating
        without arguments
        """
        test_list = [1.3, 2.34, 3.12, 8.536, 4.6, -40.0, -400.999, -12.6, 0]
        self.assertEqual(max_integer(test_list), 8.536)

    def test_max_integer_empty(self):
        """
        test case if an empty list is passed
        without arguments
        """
        self.assertEqual(max_integer([]), None)
