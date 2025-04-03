import unittest
from index import remove_element  # Importing function

class TestRemoveElement(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(remove_element([3, 2, 2, 3], 3), 2)
    def test_case_2(self):
        self.assertEqual(remove_element([0,1,2,2,3,0,4,2], 2), 6)
    def test_case_3(self):
        self.assertEqual(remove_element([1], 1), 0)

if __name__ == "__main__":
    unittest.main()