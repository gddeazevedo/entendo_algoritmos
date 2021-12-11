import unittest
from algorithms.binary_search import binary_search


class BinarySearchTestCase(unittest.TestCase):
    '''Tests for the binary_search'''

    def test_if_item_exists(self):
        item_index = binary_search([1, 3, 5, 7, 9], 3)
        self.assertEqual(item_index, 1) 

    def test_if_item_does_not_exists(self):
        item_index = binary_search([1, 3, 5, 7, 9], 10)
        self.assertEqual(item_index, None)
