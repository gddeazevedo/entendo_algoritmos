import unittest
from algorithms import recursion

class CountElementsTestCase(unittest.TestCase):
    '''Tests for the count_elements function'''

    def test_if_returns_correct_qtt_of_elements(self):
        qtt_elements = recursion.count_elements([1, 4, 5, 6])
        self.assertEqual(qtt_elements, 4)
