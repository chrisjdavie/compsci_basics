from parameterized import parameterized
import unittest


class TestKthSmallest(unittest.TestCase):

    @parameterized.expand([
        ([7, 10, 4, 3, 20, 15], 3, 7),
        ([7, 10, 4, 3, 20, 15], 4, 10)
    ])
    def test(self, arr, k, expected_value):
        self.assertEqual(kth_smallest(arr, k), expected_value)


def partition(arr, low, high):

    pivot = arr[high]

    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    i += 1
    arr[high], arr[i] = arr[i], arr[high]

    return i


def _quick_search(arr, k, low, high):
    mid = partition(arr, low, high)
    if mid == k:
        return arr[k]

    if mid < k:
        return _quick_search(arr, k, mid+1, high)
    return _quick_search(arr, k, low, mid-1)


def kth_smallest(arr, k):
    return _quick_search(arr, k-1, 0, len(arr)-1)
