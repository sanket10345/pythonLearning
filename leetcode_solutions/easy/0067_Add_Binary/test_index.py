"""
Tests for 67: Add Binary
"""

import unittest
from index import addBinary  # Importing function

class TestRemoveElement(unittest.TestCase):
    def test_case_1(self):
        a = '11'
        b = '1'
        expected_result='100'
        self.assertEqual(addBinary(a,b), expected_result)
    def test_case_2(self):
        a = '1010'
        b = '1011'
        expected_result='10101'
        self.assertEqual(addBinary(a,b), expected_result)

if __name__ == "__main__":
    unittest.main()
