import unittest
from index import removeDuplicates_wrapper  # Importing function

class TestRemoveElement(unittest.TestCase):
    def test_case_1(self):
        nums = [1,1,2]
        expected_result=[1,2]
        self.assertEqual(removeDuplicates_wrapper(nums), expected_result)
    def test_case_2(self):
        nums = [0,0,1,1,1,2,2,3,3,4]
        expected_result=[0,1,2,3,4]
        self.assertEqual(removeDuplicates_wrapper(nums), expected_result)

if __name__ == "__main__":
    unittest.main()