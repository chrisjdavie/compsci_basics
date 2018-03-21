import bisect
from parameterized import parameterized
import unittest


class Test(unittest.TestCase):

    @parameterized.expand([
        ("provided example 0", [5, 1, 4, 2, 8], [1, 2, 4, 5, 8]),
        ("provided example 1", [3, 1], [1, 3]),
        ("provided example 2", [4, 1, 3, 9, 7], [1, 3, 4, 7, 9]),
        ("provided example 3", [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
        ("provided example 4", [4, 3, 2, 10, 12, 1, 5, 6], [1, 2, 3, 4, 5, 6, 10, 12]),
        ("provided example 5", [4, 3, 2, 10, 12, 1, 5, 6], [1, 2, 3, 4, 5, 6, 10, 12]),
        ("provided example 6", [12, 11, 13, 5, 6], [5, 6, 11, 12, 13]),
        ("single value", [5], [5]),
        ("already sorted", [1, 3, 8], [1, 3, 8])
    ])
    def test(self, _, arr, sorted_arr):
        self.assertEqual(insertion_sort(arr), sorted_arr)


def insertion_sort(arr):

    for i in range(1, len(arr)):
        insert_num = arr[i]
        for j in range(i, 0, -1):
            if arr[j-1] <= insert_num:
                arr[j] = insert_num
                break
            arr[j] = arr[j-1]
        else:
            arr[0] = insert_num
    return arr
