import unittest
import algorithms


class FactorialTestCase(unittest.TestCase):
    '''Tests for the factorial recursive function'''

    def test_if_returns_expected_factorial_number(self):
        n_factorial = algorithms.recursion.factorial(5)
        self.assertEqual(n_factorial, 120)

    def test_if_returns_string_on_negative_number(self):
        string = algorithms.recursion.factorial(-1)
        self.assertEqual(string, 'Does not exist factorial of negative number')
