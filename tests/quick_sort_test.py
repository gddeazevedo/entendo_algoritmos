import unittest
import random
import algorithms


class QuickSortTestCase(unittest.TestCase):
    '''Tests for the quick_sort function'''

    def test_if_array_is_sorted(self):
        array = [random.randint(1, 100) for _ in range(10)]
        sorted_array = algorithms.quick_sort(array[:])
        self.assertEqual(sorted_array, sorted(array))
