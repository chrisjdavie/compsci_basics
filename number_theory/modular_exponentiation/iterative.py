"""
Given three numbers x, y and p, compute (x^y) % p. 

https://www.geeksforgeeks.org/modular-exponentiation-power-in-modular-arithmetic/

This is showing how to do maths with large numbers, minimising the large
numbers. Is interesting to play with - shows the difference in thinking/
training between compsci folks and physics folks - I'd never have thought to
approach this like this. The question confused me, tbh.
"""
from parameterized import parameterized
import unittest


class Test(unittest.TestCase):

    @parameterized.expand([
        (2, 3, 5, 3),
        (2, 5, 13, 6)
    ])
    def test(self, x, y, p, expected_result):
        self.assertEqual(power_mod(x, y, p), expected_result)


def power_mod(x, y, p):

    res = 1
    x = x%p

    while y > 1:
        if y%2:
            y -= 1
            res = (res*x)%p
        else:
            y /= 2
            x = (x*x)%p

    return (res*x)%p
