import unittest
from parameterized import parameterized

class Test(unittest.TestCase):

    @parameterized.expand([
        ("geek", "gesek", 1),
        ("cat", "cut", 1),
        ("sunday", "saturday", 3),
        ("abc", "abc", 0),
        ("", "", 0),
        ("", "ab", 2),
        ("a", "", 1),
        ("", "a", 1),
        ("a", "b", 1)
    ])
    def test(self, str_i, str_j, expected_distance):
        self.assertEqual(ed(str_i, str_j, 0, 0), expected_distance)

def ed(str_i, str_j, i, j):
    if i == len(str_i):
        return len(str_j) - j
    if j == len(str_j):
        return len(str_i) - i

    dist = ed(str_i, str_j, i+1, j+1)
    if str_i[i] == str_j[j]:
        return dist

    dist += 1
    dist_i = 1 + ed(str_i, str_j, i+1, j)
    dist_j = 1 + ed(str_i, str_j, i, j+1)

    return min([dist, dist_i, dist_j])

