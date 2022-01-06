import unittest
from algorithms import recursion


class FactorialTestCase(unittest.TestCase):
    '''Tests for the factorial recursive function'''

    def test_if_returns_expected_factorial_number(self):
        n_factorial = recursion.factorial(5)
        self.assertEqual(n_factorial, 120)

    def test_if_returns_string_on_negative_number(self):
        string = recursion.factorial(-1)
        self.assertEqual(string, 'Does not exist factorial of negative number')
