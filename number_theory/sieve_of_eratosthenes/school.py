"""
The school yard prime calculator.

Doing some benchmarking
"""
from math import sqrt
import unittest


class Test(unittest.TestCase):

    def test(self):
        primes = [ 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349 ]
        
        self.assertEqual(list(generate_primes(primes[-1]+1)), primes)


def generate_primes(N):

    primes = [ 2, 3 ]

    for p in primes:
        yield p

    primes = []

    for i in range(5, N, 6):
        for j in [0, 2]:
            k = i + j
            for p in primes:
                if k%p == 0:
                    break
            else:
                if k < N:
                    yield k
                primes.append(k)

if __name__ == "__main__":
    import timeit

    print(timeit.timeit("for i in generate_primes(10**4): pass", number=10000, globals=globals()))
