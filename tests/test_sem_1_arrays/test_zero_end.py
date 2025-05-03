import unittest
from seminars.sem_1_arrays.zero_end import zero_end

class TestZeroEnd(unittest.TestCase):
    def test_zero_end(self):
        self.assertEqual(zero_end([0, 1, 2, 0, 4, 0]), [1, 2, 4, 0, 0, 0])
        self.assertEqual(zero_end([1, 2, 3, 4]), [1, 2, 3, 4])
        self.assertEqual(zero_end([0, 0, 0, 1]), [1, 0, 0, 0])
        self.assertEqual(zero_end([1, 0, 2, 0, 3]), [1, 2, 3, 0, 0])
        self.assertEqual(zero_end([0, 0, 0, 0]), [0, 0, 0, 0])
        self.assertEqual(zero_end([1, 2, 3, 0, 0]), [1, 2, 3, 0, 0])
        self.assertEqual(zero_end([0, 1, 0, 2, 0, 3, 0, 4]), [1, 2, 3, 4, 0, 0, 0, 0])
        self.assertEqual(zero_end([5, 0, 1, 0, 2, 0, 3, 0, 4, 0]), [5, 1, 2, 3, 4, 0, 0, 0, 0, 0])
        self.assertEqual(zero_end([]), [])
        self.assertEqual(zero_end([0]), [0])
        self.assertEqual(zero_end([1]), [1])

if __name__ == "__main__":
    unittest.main()
