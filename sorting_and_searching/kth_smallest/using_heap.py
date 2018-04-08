import copy
from heapq import heapify, heappushpop

from parameterized import parameterized
import unittest


class TestKthSmallest(unittest.TestCase):

    @parameterized.expand([
        ([7, 10, 4, 3, 20, 15], 3, 7),
        ([7, 10, 4, 3, 20, 15], 4, 10)
    ])
    def test(self, arr, k, expected_value):
        self.assertEqual(kth_smallest(arr, k), expected_value)


def kth_smallest(arr, k):
    heap = [ -value for value in arr[:k] ]
    heapify(heap)

    for value in arr[k:]:
        if -value > heap[0]:
            heappushpop(heap, -value)

    return -heap[0]
