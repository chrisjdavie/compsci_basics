from copy import copy
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
        self.assertIs(partition(arr,[]), expected_result)

def partition(arr_l, arr_r):
    if not arr_l:
        return False
    if sum(arr_l) == sum(arr_r):
        return True

    for val in arr_l:
        arr_l_loop = copy(arr_l)
        arr_r_loop = copy(arr_r)

        arr_l_loop.remove(val)
        arr_r_loop.append(val)

        if partition(arr_l_loop, arr_r_loop):
            return True

    return False


