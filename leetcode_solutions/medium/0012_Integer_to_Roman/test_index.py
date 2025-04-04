"""
Tests for 12: Integer to Roman
"""
import unittest
from index import intToRoman  # Importing function

class TestRemoveElement(unittest.TestCase):
    def test_case_1(self):
        s = 3749
        expected_result='MMMDCCXLIX'
        self.assertEqual(intToRoman(s), expected_result)
    def test_case_2(self):
        s = 58
        expected_result='LVIII'
        self.assertEqual(intToRoman(s), expected_result)
    def test_case_3(self):
        s = 1994
        expected_result='MCMXCIV'
        self.assertEqual(intToRoman(s), expected_result)

if __name__ == "__main__":
    unittest.main()