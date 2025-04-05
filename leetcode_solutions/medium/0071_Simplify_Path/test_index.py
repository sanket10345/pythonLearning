"""
Tests for 71: Simplify Path
"""

import unittest
from index import simplifyPath  # Importing function

class TestRemoveElement(unittest.TestCase):
    def test_case_1(self):
        s ='/home/'
        expected_result='/home'
        self.assertEqual(simplifyPath(s), expected_result)
    def test_case_2(self):
        s ='/home//foo/'
        expected_result='/home/foo'
        self.assertEqual(simplifyPath(s), expected_result)
    def test_case_3(self):
        s ='/home/user/Documents/../Pictures'
        expected_result='/home/user/Pictures'
        self.assertEqual(simplifyPath(s), expected_result)
    def test_case_4(self):
        s ='/../'
        expected_result='/'
        self.assertEqual(simplifyPath(s), expected_result)
    def test_case_5(self):
        s ='/.../a/../b/c/../d/./'
        expected_result='/.../b/d'
        self.assertEqual(simplifyPath(s), expected_result)

if __name__ == "__main__":
    unittest.main()

