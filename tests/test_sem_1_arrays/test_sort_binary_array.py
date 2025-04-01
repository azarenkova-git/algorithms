import unittest
from seminars.sem_1_arrays.sort_binary_array import sort_binary_array

class TestSortBinaryArray(unittest.TestCase):
    def test_sort_binary(self):
        self.assertEqual(sort_binary_array([0, 1, 0, 1, 0, 1]), [0, 0, 0, 1, 1, 1])
        self.assertEqual(sort_binary_array([1, 1, 1, 0, 0, 0]), [0, 0, 0, 1, 1, 1])
        self.assertEqual(sort_binary_array([0, 0, 0, 1, 1, 1]), [0, 0, 0, 1, 1, 1])
        self.assertEqual(sort_binary_array([1, 0, 1, 0, 1, 0]), [0, 0, 0, 1, 1, 1])
        self.assertEqual(sort_binary_array([0]), [0])
        self.assertEqual(sort_binary_array([1]), [1])
        self.assertEqual(sort_binary_array([]), [])
        self.assertEqual(sort_binary_array([0, 0, 0, 0]), [0, 0, 0, 0])
        self.assertEqual(sort_binary_array([1, 1, 1, 1]), [1, 1, 1, 1])

if __name__ == "__main__":
    unittest.main()