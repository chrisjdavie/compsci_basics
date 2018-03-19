import unittest
from parameterized import parameterized
from queue import LifoQueue

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

    def stop(self):
        return self.min_part < 0.51

    def stop_explore(self, diff):
        return diff < 0 and abs(diff) > self.min_part


def minimum_sum_partition(nums):

    summ_2 = sum(nums)/2
    n = len(nums)
    min_part = MinPart(summ_2)

    dfs_queue = LifoQueue()
    dfs_queue.put((n-1, summ_2))
    dfs_queue.put((n-1, summ_2-nums[n-1]))

    while not dfs_queue.empty():
        n, diff_2 = dfs_queue.get()

        min_part.set_if_min(diff_2)
        if min_part.stop():
            break

        if not min_part.stop_explore(diff_2) and n-1>=0:
            dfs_queue.put((n-1, diff_2))
            dfs_queue.put((n-1, diff_2-nums[n-1]))

    return int(min_part.min_part*2)

