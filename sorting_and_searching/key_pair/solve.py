"""Given an array A[] of n numbers and another number x, determine whether or not there exist two elements in A whose sum is exactly x."""

from parameterized import parameterized
import unittest


class Test(unittest.TestCase):

    @parameterized.expand([
        (16, [1, 4, 45, 6, 10, 8], True),
        (10, [1, 2, 4, 3, 6], True),
        (1, [1, 0], True),
        (2, [0, 1], False),
        (5, [0, 2, 1], False),
        (3, [0, 2, 1], True)
    ])
    def test(self, target, arr, expected_result):
        self.assertEqual(sum_values_match_target(target, arr), expected_result)


def sum_values_match_target(target, arr):

    arr.sort()

    i_lhs = 0
    i_rhs = len(arr) - 1

    while i_lhs < i_rhs:
        summ = arr[i_lhs] + arr[i_rhs]
        if summ == target:
            return True
        elif summ > target:
            i_rhs -= 1
        else:
            i_lhs += 1

    return False
