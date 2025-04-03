import unittest
from index import rotate  # Importing function

class TestRemoveElement(unittest.TestCase):
    def test_case_1(self):
        nums = [1,2,3,4,5,6]
        k=7
        expected_result = [6,1,2,3,4,5]
        self.assertEqual(rotate(nums,k), expected_result,"Fail: test_case_1")
    def test_case_2(self):
        nums = [-1,-100,3,99]
        k = 2
        expected_result = [3,99,-1,-100]
        self.assertEqual(rotate(nums,k), expected_result,"Fail: test_case_2")
    def test_case_3(self):
        nums = [1,2,3,4,5,6]
        k=1
        expected_result = [6,1,2,3,4,5]
        self.assertEqual(rotate(nums,k), expected_result,"Fail: test_case_3")
if __name__ == "__main__":
    unittest.main()