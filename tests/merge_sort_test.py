import unittest
import random
import algorithms


class MergeSortTestCase(unittest.TestCase):
    '''Tests for the merge_sort function'''

    def test_if_array_is_sorted(self):
        array = [random.randint(1, 100) for _ in range(10)]
        sorted_array = algorithms.merge_sort(array)
        self.assertEqual(sorted_array, sorted(array))
