"""
This is a probabilistic method, and isn't used alone in pratical applications
(is sometimes used as a pre-filter in cryptography).

Using random numbers, check that:

Fermat's Little Theorem:
If n is a prime number, then for every a, 1 <= a < n,

a^(n-1) ≡ 1 (mod n)
 OR 
a^(n-1) % n = 1 

This doesn't always hold. There are False Fermats, which hold for the above 
but it's not a prime (hence k tries). There are also Carmichael numbers which
always hold for the above but aren't primes.

(Infinitely many. A smaller infinite that the infinite of primes, but still
enough that this method isn't used alone)

https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
"""
from parameterized import parameterized
from random import randint
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


def is_prime(target, k=5):
    if target < 2:
        return False
    if target < 4:
        return True
    if target == 4:
        return False

    for _ in range(k):
        a = randint(2, target-2)
        if a**(target-1)%target != 1:
            return False

    return True
