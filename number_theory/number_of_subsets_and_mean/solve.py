from collections import Counter
from parameterized import parameterized
import unittest


class Test(unittest.TestCase):

    @parameterized.expand([
        ("provided example", [3, 1, 2, 3, 4], 1, 1),
        ("two max vals", [2, 2, 1], 3, 1),
        ("three max vals", [2, 2, 2, 1], 7, 1)
    ])
    def test(self, _, arr, num_mean_max_expected, num_mean_min_expected):
        num_mean_max, num_mean_min = num_subsets(arr)
        self.assertEqual(num_mean_max, num_mean_max_expected)
        self.assertEqual(num_mean_min, num_mean_min_expected)


def num_subsets(arr):
    counts = Counter(arr)
    high = max(counts)
    num_max_subsets = 2**counts[high] - 1
    low = min(counts)
    num_min_subsets = 2**counts[low] - 1

    return num_max_subsets, num_min_subsets
