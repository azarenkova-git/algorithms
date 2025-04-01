import unittest
from seminars.sem_1_arrays.even_first import even_first

class TestEvenFirst(unittest.TestCase):
    def test_even_first(self):
        self.assertEqual(even_first([1, 2, 3, 4, 5, 6]), [2, 4, 6, 1, 3, 5])
        self.assertEqual(even_first([2, 4, 6, 8]), [2, 4, 6, 8])
        self.assertEqual(even_first([1, 3, 5, 7]), [1, 3, 5, 7])
        self.assertEqual(even_first([3, 2, 4, 1, 6, 5]), [2, 4, 6, 3, 1, 5])
        self.assertEqual(even_first([0, 1, 2, 3, 4, 5]), [0, 2, 4, 1, 3, 5])
        self.assertEqual(even_first([1]), [1])
        self.assertEqual(even_first([2]), [2])
        self.assertEqual(even_first([]), [])
        self.assertEqual(even_first([5, 4, 3, 2, 1, 0]), [4, 2, 0, 5, 3, 1])

if __name__ == "__main__":
    unittest.main()