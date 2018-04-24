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

    if y == 1:
        return x%p
    if y%2:
        return (x*power_mod(x, y-1, p))%p
    tmp = power_mod(x, y//2, p)
    return (tmp*tmp)%p
