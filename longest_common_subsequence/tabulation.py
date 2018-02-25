
import unittest
from parameterized import parameterized

class TestLCS(unittest.TestCase):

    @parameterized.expand([
        ( "ACBDGH", "AEDFHR", "ADH" ),
        ( "ABC", "AC", "AC" )
    ])
    def test(self, lhs, rhs, expected):
        self.assertEqual(expected, LCS(lhs, rhs))


def LCS(lhs, rhs, i=0, j=0):

    table = [ [""]*(len(rhs)+1) for _ in range(len(lhs)+1) ]

    for i in range(1,len(lhs)+1):
        for j in range(1,len(rhs)+1):
            table[i][j] = table[i][j-1]
            if len(table[i-1][j]) > len(table[i][j-1]):
                table[i][j] = table[i-1][j]

            if lhs[i-1] == rhs[j-1]:
                table[i][j] += lhs[i-1]

    return table[-1][-1]
    
