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


stop = False

def _partition(arr, summ_2, n):
    global stop
    if not summ_2 or stop:
        stop = True
        return True
    if n == 0 or summ_2 < 0:
        return False
    return _partition(arr, summ_2 - arr[n-1], n-1) or _partition(arr, summ_2, n-1)



def partition(arr):
    global stop
    stop = False

    summ = sum(arr)

    if summ%2 or not arr:
        return False

    summ_2 = summ//2

    return _partition(arr, summ_2 - arr[-1], len(arr)-1) or _partition(arr, summ_2, len(arr)-1)

