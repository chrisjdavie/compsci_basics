from parameterized import parameterized
from queue import LifoQueue
import unittest

class Test(unittest.TestCase):

    @parameterized.expand([
        ([1, 5, 11, 5], True),
        ([1, 5, 3], False),
        ([], False),
        ([1], False),
        ([1,1], True),
        ([1,2], False),
        ([1,1,1], False),
        ([1,1,2], True),
        ([1,1,1,1], True)
    ])
    def test(self, arr, expected_result):
        self.assertIs(partition(arr), expected_result)


def partition(arr):
    if not arr or sum(arr)%2:
        return False

    to_solve = LifoQueue()

    half_sum = sum(arr)//2

    to_solve.put((half_sum, len(arr)))

    while(not to_solve.empty()):
        diff, n = to_solve.get()
        if not diff:
            return True
        if diff < 0 or n < 0:
            continue

        to_solve.put((diff, n-1))
        to_solve.put((diff-arr[n-1], n-1))

    return False        
        

