from collections import defaultdict
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
         3 ),
        ("failed example",
         [[67, 280, 171, 381, 930, 781, 925, 4, 393, 380, 246, 433, 762, 258, 5, 166, 315], [503, 385, 728, 854, 350, 464, 288, 304, 80, 689, 56, 313, 843, 92, 379, 122, 614], [111, 403, 394, 387, 406, 138, 767, 651, 571, 880, 260, 927, 398, 926, 429, 782, 653], [634, 132, 468, 274, 435, 548, 314, 490, 212, 156, 933, 942, 629, 546, 404, 31, 292], [142, 436, 781, 260, 86, 703, 140, 697, 630, 537, 622, 410, 318, 275, 44, 801, 94], [669, 236, 993, 982, 77, 204, 137, 10, 497, 765, 907, 900, 147, 550, 42, 582, 331], [301, 19, 33, 792, 715, 14, 680, 336, 424, 350, 962, 467, 150, 408, 135, 737, 400], [468, 814, 956, 956, 175, 452, 72, 433, 704, 218, 983, 97, 799, 665, 749, 169, 49], [541, 883, 63, 572, 570, 486, 921, 884, 304, 423, 291, 790, 159, 42, 257, 324, 997], [212, 498, 801, 283, 283, 504, 500, 617, 952, 650, 281, 700, 818, 329, 592, 52, 743], [164, 621, 228, 436, 856, 883, 858, 498, 672, 17, 540, 928, 340, 536, 139, 190, 336], [773, 472, 191, 272, 88, 142, 921, 720, 842, 90, 400, 433, 141, 143, 948, 114, 722], [384, 969, 605, 593, 819, 276, 961, 358, 556, 301, 893, 46, 842, 581, 819, 665, 771], [90, 104, 265, 363, 823, 106, 452, 574, 890, 945, 68, 190, 58, 790, 925, 378, 746], [517, 196, 373, 478, 905, 280, 130, 798, 326, 323, 730, 144, 987, 500, 585, 90, 764], [947, 264, 221, 751, 837, 463, 47, 257, 652, 456, 46, 576, 185, 143, 444, 381, 867], [921, 285, 147, 402, 434, 472, 724, 163, 615, 710, 15, 551, 151, 130, 498, 414, 703]],
         13785 )
    ])
    def test(self, _, matrix, expected):
        self.assertEqual(longest_path(matrix), expected)


def memoize(func):

    longest_path_to_cell = None

    def memoized_func(matrix, ind_row, ind_column):
        nonlocal longest_path_to_cell
        # initialize history
        if ind_row == 0 and ind_column == 0:
            longest_path_to_cell = defaultdict(lambda: None)
        # set history if doesn't exist
        key = (ind_column, ind_row)
        if key not in longest_path_to_cell:
            longest_path_to_cell[key] = func(matrix, ind_row, ind_column)
        # recall history
        return longest_path_to_cell[key]

    return memoized_func


@memoize
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

