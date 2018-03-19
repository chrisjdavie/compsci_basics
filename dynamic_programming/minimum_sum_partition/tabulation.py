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


def minimum_sum_partition(nums):

    # set up problem
    sum_nums = sum(nums)
    half_sum = sum_nums/2

    table = [ [False]*sum_nums for _ in range(len(nums)) ]

    # populate table
    table[0][nums[0]] = True
    for i, num in enumerate(nums[1:]):
        for j in range(num):
            table[i+1][j] = table[i][j]
        table[i+1][num] = True
        for j in range(num+1, sum_nums):
            table[i+1][j] = table[i][j] or table[i][j-num]

    # find minimum difference
    min_diff = sum_nums
    for j in range(sum_nums):
        if table[-1][j]:
            min_diff = min([min_diff, abs(half_sum-j)])

    return int(min_diff*2)

