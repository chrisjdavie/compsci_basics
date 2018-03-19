
import unittest
from parameterized import parameterized

class TestFib(unittest.TestCase):

    @parameterized.expand([(0,0), (1,1), (2,1), (3,2), (4,3), (5,5), (6,8)])
    def test(self, input, expected):
        
        self.assertEqual(expected, fib(input))

def fib(n, storage = [ 0, 1 ]):

    for i in range(len(storage), n+1):
        storage.append(storage[-1] + storage[-2])

    return storage[n]
