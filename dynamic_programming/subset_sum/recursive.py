import unittest
from parameterized import parameterized

class Test(unittest.TestCase):

    @parameterized.expand([
        ("provided example", [3, 34, 4, 12, 5, 2], 9, True),
        ("single value true", [1], 1, True),
        ("single value false", [1], 2, False),
        ("three values true", [1, 2, 3], 5, True),
        ("three values false", [2, 4, 6], 5, False)
    ])
    def test(self, _, arr, target, expected_result):
        self.assertIs(subset_sum(arr, target), expected_result)


def _subset_sum(arr, target, n):
    if n < 0 or target < 0:
        return False
    if target == 0:
        return True

    return _subset_sum(arr, target - arr[n-1], n-1) or _subset_sum(arr, target, n-1)


def subset_sum(arr, target):
    return _subset_sum(arr, target, len(arr))

