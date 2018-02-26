from itertools import product

import unittest
from parameterized import parameterized

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
    if not arr:
        return False

    for split in product([True, False], repeat=len(arr)):
        
        sum_l, sum_r = 0, 0

        for l, val in zip(split, arr):
            if l:
                sum_l += val
            else:
                sum_r += val

        if sum_l == sum_r:
            return True
    return False    

