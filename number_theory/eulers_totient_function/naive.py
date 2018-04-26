"""
Euler’s Totient function ?(n) for an input n is count of numbers in {1, 2, 3, …, n} that are relatively prime to n, i.e., the numbers whose GCD (Greatest Common Divisor) with n is 1.

https://www.geeksforgeeks.org/eulers-totient-function/
"""
from parameterized import parameterized
import unittest

from .gcd import gcd

class Test(unittest.TestCase):

    @parameterized.expand([
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 2),
        (5, 4),
        (6, 2)
    ])
    def test(self, n, expected):
        self.assertEqual(etf(n), expected)


def etf(n):
    return len([ i for i in range(1, n+1) if gcd(i, n) == 1 ])
