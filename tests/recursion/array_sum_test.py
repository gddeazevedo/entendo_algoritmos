import unittest
from algorithms import recursion


class ArraySumTestCase(unittest.TestCase):
    '''Tests for the array_sum function'''

    def test_if_sum_is_correct(self):
        s = recursion.array_sum([10, 4, 1, 2, 3, 5, 7, 6, 8, 9])
        self.assertEqual(s, 55)
