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
    if sum(arr)%2 or not(arr):
        return False

    target = sum(arr)//2
    if any([ num > target for num in arr ]):
        return False
    
    tabulation = [ [False]*target for _ in range(len(arr)) ]

    arr.sort(reverse=True)

    # zeroth row
    tabulation[0][arr[0]-1] = True

    # all other rows
    for i, num in enumerate(arr[1:]):
        for j in range(num-1):
            tabulation[i+1][j] = tabulation[i][j]
        tabulation[i+1][num-1] = True
        for j in range(num, target):
            tabulation[i+1][j] = tabulation[i][j] or tabulation[i][j-num]
        if tabulation[i+1][-1]:
            return True
    return False

