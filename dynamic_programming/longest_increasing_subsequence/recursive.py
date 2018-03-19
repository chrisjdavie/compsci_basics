from collections import OrderedDict
import unittest
from parameterized import parameterized

class Test(unittest.TestCase):

    @parameterized.expand([
        ([10, 22, 9, 33, 21, 50, 41, 60, 80], 6),
        ([10], 1),
        ([10, 22], 2),
        ([10, 9], 1),
        ([10, 22, 9], 2),
        ([10, 22, 9, 10, 11], 3),
        ([], 0),
        ([1, 3, 2, 3], 3)
    ])
    def test(self, sequence, expected_length):
        self.assertEqual(LIS(sequence), expected_length)


def LIS(sequence):
    if not sequence:
        return 0

    maximum = 1


    def LIS_i(sequence, i):
        nonlocal maximum
        def LIS_j(sequence, k, j):
            if j < k:
                max_j = 1 + LIS_i(sequence, j)
                max_here = LIS_j(sequence, k, j + 1)
                if sequence[j] < sequence[k]:
                    max_here = max([max_j, max_here])
                return max_here
            return 1

        max_here = LIS_j(sequence, i, 0)
        maximum = max([maximum, max_here])
        return max_here

    LIS_i(sequence, len(sequence) - 1)

    return maximum
