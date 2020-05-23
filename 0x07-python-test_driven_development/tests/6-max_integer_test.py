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
        self.assertEqual(max_integer(test_list), max(test_list))

    def test_max_integer_neg(self):
        """
        test case for a list of positive and negative integers
        without arguments
        """
        test_list = [1, 2, 3, 8, 4, -40, -400, -12, 0]
        self.assertEqual(max_integer(test_list), max(test_list))

    def test_max_integer_float(self):
        """
        test case for a list of positive and negative floating
        without arguments
        """
        test_list = [1.3, 2.34, 3.12, 8.536, 4.6, -40.0, -400.999, -12.6, 0]
        self.assertEqual(max_integer(test_list), max(test_list))

    def test_max_integer_empty(self):
        """
        test case if an empty list is passed
        without arguments
        """
        test_list = []
        self.assertEqual(max_integer(test_list), None)

    def test_max_integer_one(self):
        """
        test case if list just have one element
        without arguments
        """
        test_list = [3]
        self.assertEqual(max_integer(test_list), max(test_list))

    def test_max_integer_first(self):
        """
        test case if the first element is the max
        without arguments
        """
        test_list = [5, 1, 4, 2]
        self.assertEqual(max_integer(test_list), max(test_list))

    def test_max_integer_last(self):
        """
        test case if the last element is the max
        without arguments
        """
        test_list = [1, 4, 2, 4, 4, 4, 9]
        self.assertEqual(max_integer(test_list), max(test_list))
