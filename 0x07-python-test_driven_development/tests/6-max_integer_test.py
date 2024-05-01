#!/usr/bin/python3
import unittest
'''unit test module'''
max_integer = __import__('6-max_integer').max_integer


class testmax(unittest.TestCase):
    '''test case for max integer'''
    def test_basic(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)

    def test_noarg(self):
        self.assertEqual(max_integer(), None)

    def test_empty(self):
        self.assertEqual(max_integer([]), None)

    def test_one_elem(self):
        self.assertEqual(max_integer([3]), 3)


if __name__ == "__main__":
    unittest.main()
