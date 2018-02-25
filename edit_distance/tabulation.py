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
        ("a", "b", 1),
        ("u", "au", 1),
        ("zvfrkmlnozjkpqpxrjxkitzyxacbhhkicqcoendtomfgdwdwfcgpxi", "uytdlcgdewhtaciohordtqkvwcsgspqoqmsboaguw", 47)

    ])
    def test(self, str_i, str_j, expected_distance):
        self.assertEqual(ed(str_i, str_j), expected_distance)


def ed(str_i, str_j):

    table = [ [None]*(len(str_j)+1)
                for _ in range(len(str_i)+1) ]    

    for i in range(len(str_i)+1):   
        table[i][0] = i

    for i in range(len(str_j)+1):
        table[0][i] = i

    for i in range(1, len(str_i)+1):
        for j in range(1, len(str_j)+1):
            table[i][j] = 1 + min([table[i-1][j], table[i][j-1], table[i-1][j-1]])
            if str_i[i-1] == str_j[j-1]:
                table[i][j] = table[i-1][j-1]

            
    return table[-1][-1]

