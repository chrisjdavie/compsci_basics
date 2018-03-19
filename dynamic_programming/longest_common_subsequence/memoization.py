import unittest
from parameterized import parameterized

class TestLCS(unittest.TestCase):

    @parameterized.expand([
        ( "ACBDGH", "AEDFHR", "ADH" ),
        ( "ABC", "AC", "AC" )
    ])
    def test(self, lhs, rhs, expected):
        self.assertEqual(expected, LCS(lhs, rhs))

def memoize(func):

    history = {}

    def wrapped(lhs, rhs, i=0, j=0):
        nonlocal history
        if not i and not j:
            history = {}

        key = (i,j)
        if key not in history:
            history[key] = func(lhs, rhs, i, j)
        return history[key]

    return wrapped

@memoize
def LCS(lhs, rhs, i=0, j=0):
    if i == len(lhs) or j == len(rhs):
        return ""
    if lhs[i] == rhs[j]:
        return lhs[i] + LCS(lhs, rhs, i+1, j+1)
    
    best_lhs = LCS(lhs, rhs, i+1, j)
    best_rhs = LCS(lhs, rhs, i, j+1)

    if len(best_lhs) > len(best_rhs):
        return best_lhs
    return best_rhs
    
