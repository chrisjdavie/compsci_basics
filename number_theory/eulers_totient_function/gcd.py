"""
Euclidean algorithm

In mathematics, the Euclidean algorithm[a], or Euclid's algorithm, is an efficient method for computing the greatest common divisor (GCD) of two numbers, the largest number that divides both of them without leaving a remainder.

https://en.wikipedia.org/wiki/Euclidean_algorithm#Description
"""
from parameterized import parameterized
import unittest


class Test(unittest.TestCase):

    @parameterized.expand([
        ("wiki example 0", 252, 105, 21),
        ("checking reverse", 105, 252, 21),
        ("co-prime", 6, 35, 1),
        ("wiki example 1", 24, 60, 12),
        ("wiki example 2", 1386, 3213, 63),
        ("wiki example 3", 1071, 462, 21)
    ])
    def test(self, _, a, b, expected_gcd):
        self.assertEqual(gcd(a,b), expected_gcd)

    @parameterized.expand([
        (0,),
        (-1,),
        (-2,)
    ])
    def test_invalid_values(self, value):
        self.assertRaises(ValueError, gcd, value, 40)

    def test_two_invalid_values(self):
        self.assertRaises(ValueError, gcd, -1, -2)


def gcd(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("Values less that zero aren't handled")
    if b > a:
        a, b = b, a

    r_km2 = a
    r_km1 = b

    while r_km1:
        r_k = r_km2%r_km1
        r_km1, r_km2 = r_k, r_km1

    return r_km2
