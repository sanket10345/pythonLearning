"""
Tests for 20: Valid Parentheses
"""

import unittest
from index import isValid  # Importing function

class TestRemoveElement(unittest.TestCase):
    def test_case_1(self):
        s ='()'
        expected_result=True
        self.assertEqual(isValid(s), expected_result)
    def test_case_2(self):
        s ='()[]\{\}'
        expected_result=True
        self.assertEqual(isValid(s), expected_result)
    def test_case_3(self):
        s ='(]'
        expected_result=False
        self.assertEqual(isValid(s), expected_result)
    def test_case_4(self):
        s ='([])'
        expected_result=True
        self.assertEqual(isValid(s), expected_result)

if __name__ == "__main__":
    unittest.main()
