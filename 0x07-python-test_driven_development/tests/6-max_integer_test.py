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

    def test_max_mid(self):
        self.assertEqual(max_integer([1, 2, 5, 4, 3]), 5)

    def test_max_beg(self):
        self.assertEqual(max_integer([3, 2, 1]), 3)

    def test_all_neg(self):
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_one_neg(self):
        self.assertEqual(max_integer([-1]), -1)


if __name__ == "__main__":
    unittest.main()
