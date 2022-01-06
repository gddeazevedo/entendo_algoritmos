import unittest
from algorithms import recursion


class MaxValueTestCase(unittest.TestCase):
    '''Tests for the max_value function'''

    def test_if_returns_max_value_correctly(self):
        array = [3, 4, 1, 5, 7, 8, 100, -100]
        max_value = recursion.max_value(array)
        self.assertEqual(max(array), max_value)
