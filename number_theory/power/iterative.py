from parameterized import parameterized
import unittest


class Test(unittest.TestCase):

    @parameterized.expand([
        (2, 3, 8),
        (7, 2, 49)
    ])
    def test(self, x, y, expected):
        self.assertEqual(power(x,y), expected)


def power(x, y):

    res = 1

    while y > 1:
        if y%2:
            y -= 1
            res = x*res
        x = x*x
        y = y//2

    return res*x
