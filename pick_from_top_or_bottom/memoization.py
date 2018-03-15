import unittest
from parameterized import parameterized

class Test(unittest.TestCase):

    @parameterized.expand([
        ("provided example 0", [5, 3, 7, 10], 15),
        ("provided example 1", [8, 15, 3, 7], 22),
        ("one number", [1], 1),
        ("two numbers highest", [1, 2], 2),
        ("three numbers", [1, 2, 3], 4),
        ("four numbers out of order", [3, 15, 2, 1], 16)
    ])
    def test(self, _, stack, expected_winnings):
        self.assertEqual(pick_from_top_or_bottom(stack), expected_winnings)


def cache(func):

    prev_vals = None

    def cached_func(stack, n_lhs, n_rhs):
        nonlocal prev_vals
        key = (n_lhs, n_rhs)
        if key == (0, len(stack)-1):
            prev_vals = {}
        if key not in prev_vals:
            prev_vals[key] = func(stack, n_lhs, n_rhs)
        return prev_vals[key]

    return cached_func


@cache
def _pick_from_top_or_bottom(stack, n_lhs, n_rhs):
    if n_lhs == n_rhs:
        return stack[n_lhs], 0

    best_other_l, best_mine_l = _pick_from_top_or_bottom(stack, n_lhs+1, n_rhs)
    best_mine_l += stack[n_lhs]

    best_other_r, best_mine_r = _pick_from_top_or_bottom(stack, n_lhs, n_rhs-1)
    best_mine_r += stack[n_rhs]

    if best_mine_l > best_mine_r:
        return best_mine_l, best_other_l
    return best_mine_r, best_other_r


def pick_from_top_or_bottom(stack):
    """Consider a row of n coins of values v1 . . . vn, where n is even. We play a game against an opponent by alternating turns. In each turn, a player selects either the first or last coin from the row, removes it from the row permanently, and receives the value of the coin. Determine the maximum possible amount of money we can definitely win if we move first."""
    return _pick_from_top_or_bottom(stack, 0, len(stack)-1)[0]

