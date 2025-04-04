import unittest
from index import romanToInt  # Importing function

class TestRemoveElement(unittest.TestCase):
    def test_case_1(self):
        s = 'III'
        expected_result=3
        self.assertEqual(romanToInt(s), expected_result)
    def test_case_2(self):
        s = 'LVIII'
        expected_result=58
        self.assertEqual(romanToInt(s), expected_result)
    def test_case_3(self):
        s = 'MCMXCIV'
        expected_result=1994
        self.assertEqual(romanToInt(s), expected_result)

if __name__ == "__main__":
    unittest.main()