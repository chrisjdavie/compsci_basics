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
        ([], 0)
    ])
    def test(self, sequence, expected_length):
        self.assertEqual(LIS(sequence), expected_length)


def LIS(sequence):
    if not sequence:
        return 0

    maximum = 1

    def LIS_i(sequence, i):
        nonlocal maximum
        def LIS_j(sequence, j):
            if j >= 0:
                max_i = 1 + LIS_i(sequence, j)
                max_j = LIS_j(sequence, j - 1)
                if sequence[j] < sequence[i]:
                    max_here = max([max_i, max_j])
                    return max_here
            return 1

        max_here = LIS_j(sequence, i-1)
        maximum = max([maximum, max_here])
        return max_here

    LIS_i(sequence, len(sequence) - 1)

    return maximum
