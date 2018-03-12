import unittest
from parameterized import parameterized


class Test(unittest.TestCase):

    @parameterized.expand([
        ("given example",
         [ [ 348, 391 ],
           [ 618, 193 ] ],
         1009 ),
        ("Singular matrix",
         [ [ 1 ] ],
         1 ),
        ("RHS column",
         [ [ 0, 2 ],
           [ 1, 3 ] ],
         5 ),
        ("LHS column",
         [ [ 3, 1 ],
           [ 4, 2 ] ],
         7 ),
        ("LHS, RHS",
         [ [ 4, 3 ],
           [ 2, 5 ] ],
         9 ),
        ("RHS, LHS",
         [ [ 3, 6 ],
           [ 5, 4 ] ],
         11 ), 
        ("3x3 test",
         [ [ 1, 4, 7 ],
           [ 2, 5, 8 ],
           [ 3, 6, 9 ] ],
         24 ), 
        ("highest not in soln",
         [ [ 14,  1, 1  ],
           [ 14,  1, 15 ],
           [ 14,  1, 1  ] ],
         14*3 ),
        ("two routes to soln",
         [ [ 1, 1 ],
           [ 2, 2 ] ],
         3 )
    ])
    def test(self, _, matrix, expected):
        self.assertEqual(longest_path(matrix), expected)


def _longest_path(matrix, ind_row, ind_column):
    if ind_row >= len(matrix) or ind_column < 0 or ind_column >= len(matrix):
        return 0

    result = max([_longest_path(matrix, ind_row+1, ind_column-1), 
                  _longest_path(matrix, ind_row+1, ind_column),
                  _longest_path(matrix, ind_row+1, ind_column+1)]) \
            + matrix[ind_row][ind_column]
    return result


def longest_path(matrix):
    
    return max([ _longest_path(matrix, 0, i) for i in range(len(matrix)) ])

