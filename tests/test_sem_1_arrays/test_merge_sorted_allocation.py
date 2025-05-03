import unittest
from seminars.sem_1_arrays.merge_sorted_arrays_1_allocation import merge_sorted_arrays_1_allocation

class TestMergeSortedAllocation(unittest.TestCase):
    def test_merge_sorted(self):
        self.assertEqual(merge_sorted_arrays_1_allocation([1, 2, 3, 0, 0, 0], [2, 5, 6]), [1, 2, 2, 3, 5, 6])
        self.assertEqual(merge_sorted_arrays_1_allocation([1], []), [1])
        self.assertEqual(merge_sorted_arrays_1_allocation([0], [1]), [1])
        self.assertEqual(merge_sorted_arrays_1_allocation([], []), [])
        self.assertEqual(merge_sorted_arrays_1_allocation([4, 5, 6, 0, 0, 0], [1, 2, 3]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(merge_sorted_arrays_1_allocation([1, 2, 3, 0, 0, 0], [4, 5, 6]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(merge_sorted_arrays_1_allocation([2, 2, 2, 0, 0, 0], [2, 2, 2]), [2, 2, 2, 2, 2, 2])
        self.assertEqual(merge_sorted_arrays_1_allocation([0, 0, 0, 0, 0], [1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

if __name__ == "__main__":
    unittest.main()
