from parameterized import parameterized
from queue import LifoQueue
import unittest

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


def subset_sum(arr, target):
    """Determine if there is a subset of arr with sum equal to target"""
    
    subset_queue = LifoQueue()

    subset_queue.put((target, len(arr)))

    while not subset_queue.empty():
        diff, n = subset_queue.get()

        if not diff:
            return True

        if diff >= 0 and n > 0:
            subset_queue.put((diff, n-1))
            subset_queue.put((diff-arr[n-1], n-1))

    return False

