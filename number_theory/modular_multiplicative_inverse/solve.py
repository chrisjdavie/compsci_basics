"""
Given two integers ‘a’ and ‘m’, find modular multiplicative inverse of ‘a’ under modulo ‘m’.

The modular multiplicative inverse is an integer ‘x’ such that

(a x)mod m ≡ 1

The value of x should be in {0, 1, 2, … m-1}, i.e., in the ring of integer modulo m.
"""

from parameterized import parameterized
import unittest


class Test(unittest.TestCase):

    @parameterized.expand([
        ("provided example 0", 3, 11, 4),
        ("provided example 1", 10, 17, 12),
        ("test 0", 47, 84, 59),
        ("test 1, regression", 44, 78, -1)
    ])
    def test(self, _, a, m, expected):
        self.assertEqual(mmi(a, m), expected)


def mmi(a, m):

    for x in range(m):
        if (a*x)%m == 1:
            break
    else:
        x = -1

    return x
