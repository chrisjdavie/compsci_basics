import copy
from parameterized import parameterized
import unittest

from .recursive import partition, quick_sort


class TestPartition(unittest.TestCase):

    @parameterized.expand([
        ([1, 8, 3, 9, 4, 5, 7], 0, 6, [1, 3, 4, 5, 7, 9, 8]),
        ([1, 2], 0, 1, [1, 2]),
        ([2, 1], 0, 1, [1, 2]),
        ([3, 1, 2], 0, 2, [1, 2, 3]),
        ([3, 1, 2], 1, 2, [3, 1, 2])
    ])
    def test(self, arr, high, low, arr_expected):
        pivot = arr[-1]
        mid = partition(arr, high, low)
        self.assertEqual(arr, arr_expected)
        self.assertEqual(arr.index(pivot), mid)


class TestMergeSort(unittest.TestCase):

    @parameterized.expand([
        ("provided example 0", [5, 1, 4, 2, 8]),
        ("provided example 1", [3, 1]),
        ("provided example 2", [4, 1, 3, 9, 7]),
        ("provided example 3", [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]),
        ("provided example 4", [4, 3, 2, 10, 12, 1, 5, 6]),
        ("provided example 6", [12, 11, 13, 5, 6]),
        ("single value", [5]),
        ("already sorted", [1, 3, 8])
    ])
    def test(self, _, arr):
        sorted_arr = sorted(copy.copy(arr))
        quick_sort(arr)
        self.assertEqual(arr, sorted_arr)
