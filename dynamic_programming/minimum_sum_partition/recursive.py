import unittest
from parameterized import parameterized


class Test(unittest.TestCase):

    @parameterized.expand([
        ([1, 6, 5, 11], 1),
        ([36, 7, 46, 40], 23),
        ([1, 1], 0),
        ([1, 2], 1),
        ([2, 1], 1),
        ([1, 1, 1], 1)
    ])
    def test(self, nums, expected):
        self.assertEqual(minimum_sum_partition(nums), expected)


class MinPart:

    def __init__(self, summ_2):
        self.min_part = summ_2

    def set_if_min(self, diff):
        self.min_part = min([self.min_part, abs(diff)])

    def stop(self, diff):
        return self.min_part < 0.51 or (diff < 0 and abs(diff) > self.min_part)


def _minimum_sum_partition(nums, n, run_sum, min_part):
    if n < 0:
        return

    min_part.set_if_min(run_sum)

    if min_part.stop(run_sum):
        return

    _minimum_sum_partition(nums, n-1, run_sum-nums[n-1], min_part)
    _minimum_sum_partition(nums, n-1, run_sum, min_part)


def minimum_sum_partition(nums):

    summ_2 = sum(nums)/2
    n = len(nums)
    min_part = MinPart(summ_2)

    _minimum_sum_partition(nums, n-1, summ_2 - nums[n-1], min_part)
    _minimum_sum_partition(nums, n-1, summ_2, min_part)

    return int(min_part.min_part*2)

