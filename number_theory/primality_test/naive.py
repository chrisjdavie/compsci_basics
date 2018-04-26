from math import sqrt
from parameterized import parameterized
import unittest


class Test(unittest.TestCase):

    @parameterized.expand([
        (11, True),
        (15, False),
        (1, False),
        (5, True),
        (4, False),
        (49, False)
    ])
    def test(self, target, is_prime_expected):
        self.assertEqual(is_prime(target), is_prime_expected)


def is_prime(target):
    if target < 2:
        return False

    if not target%2 or not target%3:
        return False
    for i in range(5, int(sqrt(target)) + 1, 6):
        if not target%i or not target%(i+2):
            return False
    return True
