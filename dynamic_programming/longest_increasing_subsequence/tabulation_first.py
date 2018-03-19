
import unittest
from parameterized import parameterized

class Test(unittest.TestCase):

    @parameterized.expand([
        ([10, 22, 9, 33, 21, 50, 41, 60, 80], 6),
        ([10], 1),
        ([10, 22], 2),
        ([10, 9], 1),
        ([10, 22, 9, 10, 11], 3),
        ([0], 1),
        ([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], 6),
        ([], 0)
    ])
    def test(self, sequence, expected_length):

        self.assertEqual(LIS(sequence), expected_length)
        pass

def LIS(sequence):
    if not sequence:
        return 0

    table = [0]*(max(sequence)+2)

    for number in sequence:
        table[number+1] = max(table[:number+1]) + 1

    return max(table)

