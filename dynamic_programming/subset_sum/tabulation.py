import unittest
from parameterized import parameterized

class Test(unittest.TestCase):

    @parameterized.expand([
        ("provided example", [3, 34, 4, 12, 5, 2], 9, True),
        ("single value true", [1], 1, True),
        ("single value false", [1], 2, False),
        ("three values true", [1, 2, 3], 5, True),
        ("three values false", [2, 4, 6], 5, False)
    ])
    def test(self, _, arr, target, expected_result):
        self.assertIs(subset_sum(arr, target), expected_result)


def subset_sum(arr, target):

    arr.sort()

    soln_table = [ [False]*len(arr) for _ in range(target) ]

    # initial column
    soln_table[0][arr[0]-1] = True

    for i, num in enumerate(arr[1:]):
        for j in range(min(num - 1,target)):
            soln_table[j][i+1] = soln_table[j][i]
        if num-1 < target:        
            soln_table[num-1][i+1] = True
        for j in range(num, target):
            soln_table[j][i+1] = soln_table[j-num][i] or soln_table[j][i]

    return soln_table[-1][-1]

