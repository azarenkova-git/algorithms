import unittest
from seminars.sem_1_arrays.merge_sorted_arrays import merge_sorted_arrays

class TestMergeSortedArrays(unittest.TestCase):
    def test_merge(self):
        self.assertEqual(merge_sorted_arrays([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(merge_sorted_arrays([1, 2, 3], [4, 5, 6]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(merge_sorted_arrays([4, 5, 6], [1, 2, 3]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(merge_sorted_arrays([], [1, 2, 3]), [1, 2, 3])
        self.assertEqual(merge_sorted_arrays([1, 2, 3], []), [1, 2, 3])
        self.assertEqual(merge_sorted_arrays([], []), [])
        self.assertEqual(merge_sorted_arrays([1, 1, 1], [1, 1, 1]), [1, 1, 1, 1, 1, 1])
        self.assertEqual(merge_sorted_arrays([-3, -2, -1], [0, 1, 2]), [-3, -2, -1, 0, 1, 2])
        self.assertEqual(merge_sorted_arrays([1, 3, 7], [2, 4, 8, 9]), [1, 2, 3, 4, 7, 8, 9])

if __name__ == "__main__":
    unittest.main()
