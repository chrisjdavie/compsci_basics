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

    if y == 1:
        return x
    if y%2:
        return x*power(x,y-1)
    pow_xy = power(x,y//2)
    return pow_xy*pow_xy

