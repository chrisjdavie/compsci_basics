"""
Algorithm is from https://www.geeksforgeeks.org/interpolation-search/ but
doesn't feel robust - if the array contains a wide range of numbers, it
could be that the the "delta value" is sufficiently small that the estimated
target index will always be the lower bound.

As a noddy example, it's okay, but in production I'd be unhappy with this as
a core algorithm without either a backup or lots of defensive coding.
"""
from parameterized import parameterized
import unittest

class Test(unittest.TestCase):

    @parameterized.expand([
        ([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610], 55),
        ([3, 7, 9, 15, 16, 17], 16),
    ])
    def test_passes(self, arr, target):
        expected_index = arr.index(target)
        self.assertEqual(expected_index, interpolation_search(arr, target))

    def test_fails_if_not_found(self):
        self.assertRaises(ValueError, interpolation_search, [ 1, 3, 4 ], 2)


#TODO: make sure both tests take more than one jump


def expected_target(arr, i_high, i_low, value_target):
    delta_value = (value_target - arr[i_low])/(arr[i_high] - arr[i_low])
    i_target = delta_value*(i_high - i_low) + i_low
    return int(i_target)


def interpolation_search(arr, target):

    i_target = -1
    i_target_previous = -2
    i_low = 0
    i_high = len(arr) - 1

    while i_target != i_target_previous:
        i_target_previous = i_target
        i_target = expected_target(arr, i_low, i_high, target)

        if arr[i_target] < target:
            i_low = i_target + 1
        if arr[i_target] > target:
            i_high = i_target - 1
        if arr[i_target] == target:
            return i_target

    raise ValueError("Target value {} not in array".format(target))

