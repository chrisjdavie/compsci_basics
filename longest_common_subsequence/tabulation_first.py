
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
    table = [ [ None ]*len(rhs)
        for _ in lhs ]
    
    table[-1][-1] = ""
    if lhs[-1] == rhs[-1]:
        table[-1][-1] = lhs[-1]

    for i in range(2, len(lhs)+1):
        table[-i][-1] = ""
        if lhs[-i] == rhs[-1]:
            table[-i][-1] = lhs[-i]

        table[-i][-1] += table[-(i-1)][-1]

    for j in range(2, len(rhs)+1):
        table[-1][-j] = ""
        if lhs[-1] == rhs[-j]:
            table[-1][-j] = rhs[-j]

        table[-1][-j] += table[-1][-(j-1)]

    for i in range(2, len(lhs)+1):
        for j in range(2, len(rhs)+1):
            table[-i][-j] = ""
            if lhs[-i] == rhs[-j]:
                table[-i][-j] = lhs[-i]

            if len(table[-(i-1)][-j]) > len(table[-i][-(j-1)]):
                table[-i][-j] += table[-(i-1)][-j]
            else:
                table[-i][-j] += table[-i][-(j-1)]

    return table[0][0]
    
