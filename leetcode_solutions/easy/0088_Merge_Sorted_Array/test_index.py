import unittest
from index import merge_wrapper  # Importing function

class TestRemoveElement(unittest.TestCase):
    def test_case_1(self):
        nums1 = [1,2,3,0,0,0]
        m = 3
        nums2 = [2,5,6]
        n = 3
        expected_result = [1,2,2,3,5,6]
        self.assertEqual(merge_wrapper(nums1, m, nums2, n), expected_result)
    def test_case_2(self):
        nums1 = [1]
        m = 1
        nums2 = []
        n = 0
        expected_result = [1]
        self.assertEqual(merge_wrapper(nums1, m, nums2, n), expected_result)
    def test_case_3(self):
        nums1 = [0]
        m = 0
        nums2 = [1]
        n = 1
        expected_result = [1]
        self.assertEqual(merge_wrapper(nums1, m, nums2, n), expected_result)

if __name__ == "__main__":
    unittest.main()