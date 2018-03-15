import unittest
from parameterized import parameterized

class Test(unittest.TestCase):

    @parameterized.expand([
        ("provided example 0", [5, 3, 7, 10], 15),
        ("provided example 1", [8, 15, 3, 7], 22),
        ("one number", [1], 1),
        ("two numbers highest", [1, 2], 2),
        ("three numbers", [1, 2, 3], 4),
        ("three numbers out of order", [15, 2, 1], 16),
        ("four numbers out of order", [3, 15, 2, 1], 16)
    ])
    def test(self, _, stack, expected_winnings):
        self.assertEqual(pick_from_top_or_bottom(stack), expected_winnings)


def pick_from_top_or_bottom(stack):
    """Consider a row of n coins of values v1 . . . vn, where n is even. We play a game against an opponent by alternating turns. In each turn, a player selects either the first or last coin from the row, removes it from the row permanently, and receives the value of the coin. Determine the maximum possible amount of money we can definitely win if we move first."""

    results = [ [None]*len(stack) for _ in range(len(stack)) ]

    for i in range(len(stack)):
        results[i][i] = (stack[i], 0)

    for i in range(len(stack)):
        for j in range(i-1, -1, -1):
            pick_r_other, pick_r_mine = results[i-1][j]
            pick_r_mine += stack[i]
            pick_l_other, pick_l_mine = results[i][j+1]
            pick_l_mine += stack[j]
            if pick_r_mine > pick_l_mine:
                results[i][j] = (pick_r_mine, pick_r_other)
            else:
                results[i][j] = (pick_l_mine, pick_l_other)

    return results[-1][0][0]

