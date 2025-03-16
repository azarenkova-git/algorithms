import unittest
from seminars.sem_1_arrays.rotate_part_array import rotate_part_array

class TestRotatePartArray(unittest.TestCase):
    def test_rotate_part(self):
        self.assertEqual(rotate_part_array([1, 2, 3, 4, 5], 2), [4, 5, 1, 2, 3])
        self.assertEqual(rotate_part_array([1, 2, 3, 4, 5], 3), [3, 4, 5, 1, 2])
        self.assertEqual(rotate_part_array([1, 2, 3, 4, 5], 5), [1, 2, 3, 4, 5])
        self.assertEqual(rotate_part_array([1, 2, 3, 4, 5], 0), [1, 2, 3, 4, 5])
        self.assertEqual(rotate_part_array([1, 2], 1), [2, 1])
        self.assertEqual(rotate_part_array([1], 1), [1])
        self.assertEqual(rotate_part_array([], 3), [])
        self.assertEqual(rotate_part_array([-1, -2, -3, -4, -5], 2), [-4, -5, -1, -2, -3])

if __name__ == "__main__":
    unittest.main()
