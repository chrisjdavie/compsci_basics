from parameterized import parameterized
import unittest


class Test(unittest.TestCase):

    @parameterized.expand([
        ("provided example 0", [5, 1, 4, 2, 8], [1, 2, 4, 5, 8]),
        ("provided example 1", [3, 1], [1, 3]),
        ("single value", [5], [5]),
        ("already sorted", [1, 3, 8], [1, 3, 8])
    ])
    def test(self, _, arr, sorted_arr):
        self.assertEqual(bubble_sort(arr), sorted_arr)


def bubble_sort(arr):

    for j in range(len(arr), -1, -1):
        sorted = True
        for i in range(j-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                sorted = False
        if sorted:
            break

    return arr
