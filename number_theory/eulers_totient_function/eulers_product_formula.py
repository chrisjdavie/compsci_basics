"""
Euler’s Totient function ?(n) for an input n is count of numbers in {1, 2, 3, …, n} that are relatively prime to n, i.e., the numbers whose GCD (Greatest Common Divisor) with n is 1.

https://www.geeksforgeeks.org/eulers-totient-function/
"""
from parameterized import parameterized
import unittest

class TestPhi(unittest.TestCase):

    @parameterized.expand([
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 2),
        (5, 4),
        (6, 2),
        (7, 6),
        (8, 4),
        (9, 6),
        (10, 4)
    ])
    def test(self, n, expected):
        self.assertEqual(phi(n), expected)


class TestMaximizeNDivPhi(unittest.TestCase):

    @parameterized.expand([
        (2, 2),
        (6, 6),
        (50, 30),        
        (510510, 510510)
    ])
    def test(self, n, expected):
        self.assertEqual(maximise_n_div_phi(n), expected)


def phi(n):

    res = n
    p = 2

    while p*p <= n:

        if n%p == 0:
            while n%p == 0:
                n = n//p
            res *= (1 - 1/p)
        p += 1

    # at this stage, n can either be 1 or prime
    if n > 1:
        res *= (1 - 1/n)

    return round(res)


def maximise_n_div_phi(N):
    max_n_div_phi = 0
    max_n = 0

    for n in range(1, N+1):
        n_div_phi = n/phi(n)
        if n_div_phi > max_n_div_phi:
            max_n_div_phi = n_div_phi
            max_n = n

    return max_n

