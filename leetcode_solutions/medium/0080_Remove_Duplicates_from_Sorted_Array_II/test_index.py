import unittest
from index import removeDuplicates_wrapper  # Importing function

class TestRemoveElement(unittest.TestCase):
    def test_case_1(self):
        nums = [1,1,1,2,2,3]
        expected_result=[1,1,2,2,3]
        self.assertEqual(removeDuplicates_wrapper(nums), expected_result,"Fail: test_case_1")
    def test_case_2(self):
        nums = [0,0,1,1,1,1,2,3,3]
        expected_result=[0,0,1,1,2,3,3]
        self.assertEqual(removeDuplicates_wrapper(nums), expected_result,"Fail: test_case_2")
    def test_case_3(self):
        nums = [0,1,1,1,1,1,1,1,1,1]
        expected_result=[0,1,1]
        self.assertEqual(removeDuplicates_wrapper(nums), expected_result,"Fail: test_case_3")
    def test_case_4(self):
        nums = [0,0,0,1]
        expected_result=[0,0,1]
        self.assertEqual(removeDuplicates_wrapper(nums), expected_result,"Fail: test_case_4")
if __name__ == "__main__":
    unittest.main()