"""
The school yard prime calculator.

Doing some benchmarking
"""
from memory_profiler import profile

from math import sqrt
import unittest


class Test(unittest.TestCase):

    def test(self):
        primes = [ 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349 ]
        
        self.assertEqual(list(generate_primes(primes[-1]+1)), primes)

@profile
def generate_primes(N):

    sieve_a = [ True ]*N

    for i in range(2, N):
        if sieve_a[i]:
            for j in range(round(N/i)):
                sieve_a[i*j] = False
    return



def wrapper(N):
    for i in generate_primes(510510):
        pass


if __name__ == "__main__":
    import timeit
    
    #print(timeit.timeit("for i in generate_primes(510510): pass", number=1, globals=globals()))
    generate_primes(100000)
