import unittest
import random
import algorithms


class SelectionSortTestCase(unittest.TestCase):
    '''Tests for the selection_sort function'''

    def test_if_array_is_sorted(self):
        array = [random.randint(1, 100) for _ in range(10)]
        sorted_array = algorithms.selection_sort(array[:])
        self.assertEqual(sorted_array, sorted(array))
