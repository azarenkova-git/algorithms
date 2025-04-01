import unittest
from seminars.sem_1_arrays.two_sum import two_sum

class TestTwoSum(unittest.TestCase):
    def test_two_sum(self):
        self.assertEqual(two_sum([1, 2, 3, 4, 6], 6), (1, 3))
        self.assertEqual(two_sum([2, 7, 11, 15], 9), (0, 1))
        self.assertEqual(two_sum([1, 2, 3, 4, 5], 10), (-1, -1))
        self.assertIn(two_sum([-3, -1, 0, 2, 4, 5], 1), [(1, 3), (0, 4)])
        self.assertEqual(two_sum([1, 3], 4), (0, 1))
        self.assertEqual(two_sum([1, 3], 5), (-1, -1))

if __name__ == "__main__":
    unittest.main()
