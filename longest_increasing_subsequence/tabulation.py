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

    longest_prev = OrderedDict()
    for num in sorted(sequence):
        longest_prev[num] = 0

    for num in sequence:
        prev_max = 0
        for prev_num, count in longest_prev.items():
            if prev_num >= num:
                break
            prev_max = max([prev_max, count])

        longest_prev[num] = prev_max + 1

    return max(longest_prev.values())
