"""
Tests for 8: String to Integer (atoi)
"""

import unittest
from index import myAtoi  # Importing function

class TestRemoveElement(unittest.TestCase):
    def test_case_1(self):
        s = '42'
        expected_result=42
        self.assertEqual(myAtoi(s), expected_result)
    def test_case_2(self):
        s = ' -042'
        expected_result= -42
        self.assertEqual(myAtoi(s), expected_result)
    def test_case_3(self):
        s = '1337c0d3'
        expected_result=1337
        self.assertEqual(myAtoi(s), expected_result)
    def test_case_4(self):
        s = '0-1'
        expected_result=0
        self.assertEqual(myAtoi(s), expected_result)
    def test_case_5(self):
        s = 'words and 987'
        expected_result=0
        self.assertEqual(myAtoi(s), expected_result)
    def test_case_6(self):
        s = '99999999999999999999999999999999'
        expected_result=2147483647
        self.assertEqual(myAtoi(s), expected_result)
    def test_case_7(self):
        s = '-9999999999999999999999999999999'
        expected_result= -2147483648
        self.assertEqual(myAtoi(s), expected_result)

if __name__ == "__main__":
    unittest.main()
