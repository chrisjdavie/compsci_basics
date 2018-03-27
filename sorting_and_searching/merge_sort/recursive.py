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
        self.assertEqual(merge_sort(arr), sorted_arr)


def next_biggest(lhs_sorted, rhs_sorted):

    next_lhs = next(lhs_sorted)
    next_rhs = next(rhs_sorted)

    while True:
        if next_lhs < next_rhs:
            yield next_lhs
            try:
                next_lhs = next(lhs_sorted)
            except StopIteration:
                yield next_rhs
                break
        else:
            yield next_rhs
            try:
                next_rhs = next(rhs_sorted)
            except StopIteration:
                yield next_lhs
                break

    yield from lhs_sorted
    yield from rhs_sorted


def _merge_sort(arr, start, end):
    if start == end:
        return iter([arr[start]])
    
    midpoint = (start + end)//2

    lhs_sorted = _merge_sort(arr, start, midpoint)
    rhs_sorted = _merge_sort(arr, midpoint + 1, end)

    return next_biggest(lhs_sorted, rhs_sorted)


def merge_sort(arr):

    return list(_merge_sort(arr, 0, len(arr)-1))
