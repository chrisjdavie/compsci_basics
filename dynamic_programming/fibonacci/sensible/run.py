
import unittest
from parameterized import parameterized

class TestFib(unittest.TestCase):

    @parameterized.expand([(0,0), (1,1), (2,1), (3,2), (4,3), (5,5), (6,8)])
    def test(self, input, expected):
        self.assertEqual(expected, fib(input))

def fib(n):
    if n < 2:
        return n

    minus_1, minus_2 = 1, 0
    for _ in range(2, n+1):
        output = minus_1 + minus_2
        minus_1, minus_2 = output, minus_1
    
    return output
