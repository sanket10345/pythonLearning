"""
Tests for 224: Basic Calculator
"""

import unittest
from index import calculate  # Importing function

class TestBasicCalculator(unittest.TestCase):

    def test_basic_operations(self):
        self.assertEqual(calculate('1 + 1'), 2)
        self.assertEqual(calculate(' 2-1 + 2 '), 3)
        self.assertEqual(calculate('(1+(4+7)-3)+(6+8)'), 23)

    def test_negatives_and_parentheses(self):
        self.assertEqual(calculate('-(2 + 3)'), -5)
        self.assertEqual(calculate('-(1)'), -1)
        self.assertEqual(calculate('- (3 + (4 + 5))'), -12)
        self.assertEqual(calculate('-(3) + 4'), 1)
        self.assertEqual(calculate('-7 + (3 - 2)'), -6)

    def test_nested_and_complex(self):
        self.assertEqual(calculate("((((1+1))))"), 2)
        self.assertEqual(calculate("((1 + (2 + (3 + (4)))))"), 10)
        self.assertEqual(calculate("(0-(1+2-3)+(4-5))"), -1)

    def test_whitespace(self):
        self.assertEqual(calculate("  30 +    ( 4 - 2 ) "), 32)
        self.assertEqual(calculate("   - ( 3 + 2 ) + 1 "), -4)

    def test_minimal_expressions(self):
        self.assertEqual(calculate("1"), 1)
        self.assertEqual(calculate("  0  "), 0)

    def test_unary_sign_chaining(self):
        self.assertEqual(calculate("- ( -3 + 5 )"), -2)
        self.assertEqual(calculate("-(1-(2+3))"), 4)
        self.assertEqual(calculate("-(-(-1))"), -1)

    def test_multi_digit_and_large(self):
        self.assertEqual(calculate("123 + 456 - 789"), -210)
        self.assertEqual(calculate("(1000 + 2000) - (500 + 500)"), 2000)


if __name__ == '__main__':
    unittest.main()