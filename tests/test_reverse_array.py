import unittest
from seminars.sem_1_arrays.reverse_array import reverse_array

class TestReverseArray(unittest.TestCase):
    def test_reverse_array(self):
        self.assertEqual(reverse_array([1, 2, 3, 4, 6]), [6, 4, 3, 2, 1])
        self.assertEqual(reverse_array([2, 7, 11, 15]), [15, 11, 7, 2])
        self.assertEqual(reverse_array([]), [])
        self.assertEqual(reverse_array([-5, -3, 0, 3, 5]), [5, 3, 0, -3, -5])
        self.assertEqual(reverse_array([1]), [1])
        self.assertEqual(reverse_array([1, 2]), [2, 1])


if __name__ == "__main__":
    unittest.main()