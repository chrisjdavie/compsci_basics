import bisect
import unittest
from parameterized import parameterized


class Test(unittest.TestCase):

    @parameterized.expand([
        ("provided example", [1, 2, 7, 4, 3], 2, 1),
        ("number on RHS", [1, 2, 7, 4, 3], 4, 3),
        ("missing number", [1, 2, 7, 4, 3], 5, -1),
        ("short array 2", [1, 2], 2, 1),
        ("short array 3", [1, 3, 2], 2, 2),
        ("failed test 0", [1, 9, 11, 16, 17, 18, 22, 33, 38, 40, 53, 54, 58, 68, 70, 72, 82, 84, 87, 88, 98, 100, 105, 110, 113, 115, 117, 123, 127, 128, 132, 135, 137, 142, 148, 150, 153, 155, 156, 160, 171, 172, 173, 174, 180, 182, 184, 185, 190, 196, 198, 199, 200, 212, 218, 224, 225, 226, 232, 255, 264, 265, 267, 270, 279, 281, 282, 284, 286, 290, 296, 297, 298, 299, 301, 309, 310, 311, 314, 315, 326, 327, 335, 338, 339, 342, 351, 352, 353, 355, 356, 361, 362, 365, 369, 377, 379, 383, 394, 399, 400, 405, 413, 416, 422, 427, 429, 434, 438, 440, 446, 466, 477, 483, 484, 488, 490, 491, 492, 495, 507, 512, 518, 526, 529, 533, 536, 538, 539, 540, 542, 549, 552, 553, 556, 560, 564, 567, 571, 578, 583, 584, 588, 591, 594, 596, 604, 611, 619, 622, 632, 637, 639, 640, 642, 644, 650, 652, 658, 663, 666, 668, 673, 674, 680, 683, 686, 694, 699, 709, 716, 717, 721, 723, 736, 761, 762, 763, 775, 777, 778, 784, 788, 791, 806, 814, 815, 816, 821, 826, 828, 829, 834, 840, 845, 851, 852, 853, 854, 857, 858, 860, 861, 872, 876, 878, 887, 889, 891, 893, 899, 911, 929, 931, 932, 933, 950, 953, 955, 956, 957, 958, 963, 970, 971, 973, 977, 978, 983, 986, 988, 990, 991, 992, 998, 1000, 982, 981, 968, 961, 949, 934, 920, 913, 903, 869, 824, 798, 794, 730, 727, 720, 719, 678, 667, 660, 625, 574, 563, 497, 486, 476, 475, 473, 470, 469, 425, 419, 384, 378, 359, 344, 324, 306, 305, 287, 246, 239, 217, 208, 193, 175, 161, 157, 154, 141, 134, 126, 101, 76, 63, 51, 43, 31, 30, 20, 12, 3], 721, 172),
        ("failed test 1", [1, 5, 10, 11, 13, 18, 19, 22, 35, 36, 45, 58, 64, 72, 91, 95, 118, 128, 129, 135, 140, 141, 143, 159, 166, 170, 172, 174, 191, 192, 199, 210, 224, 239, 255, 268, 281, 282, 293, 309, 321, 326, 342, 349, 357, 359, 367, 369, 375, 377, 383, 393, 397, 401, 402, 410, 411, 414, 422, 423, 447, 458, 459, 462, 471, 482, 485, 486, 491, 493, 498, 504, 505, 512, 521, 526, 534, 539, 543, 551, 554, 555, 561, 563, 564, 570, 586, 604, 606, 609, 615, 617, 621, 627, 631, 632, 635, 637, 639, 648, 661, 662, 674, 686, 695, 700, 706, 708, 709, 721, 733, 743, 744, 748, 749, 755, 756, 760, 769, 781, 787, 789, 808, 824, 833, 834, 855, 856, 863, 864, 866, 868, 888, 895, 896, 900, 902, 924, 927, 930, 931, 938, 943, 953, 959, 969, 974, 984, 990, 987, 979, 977, 957, 956, 926, 917, 907, 903, 885, 873, 870, 841, 807, 803, 798, 791, 785, 783, 782, 736, 725, 722, 711, 675, 670, 655, 645, 642, 603, 590, 577, 567, 558, 549, 546, 537, 531, 524, 523, 513, 483, 449, 440, 429, 418, 378, 376, 354, 351, 338, 300, 297, 283, 266, 261, 243, 237, 221, 165, 162, 158, 148, 112, 90, 89, 88, 52, 50, 24, 16, 15, 6], 661, 100),
        ("failed test 2", [39, 51, 71, 84, 92, 93, 149, 154, 158, 173, 178, 193, 216, 217, 231, 243, 410, 425, 429, 459, 476, 482, 483, 540, 542, 567, 586, 587, 593, 746, 807, 823, 833, 839, 850, 873, 919, 923, 975, 1000, 994, 992, 990, 989, 987, 984, 980, 979, 976, 970, 965, 960, 958, 955, 945, 939, 928, 915, 910, 909, 905, 896, 889, 885, 879, 874, 872, 870, 862, 861, 852, 846, 841, 838, 829, 828, 826, 825, 821, 820, 819, 817, 816, 815, 814, 812, 811, 804, 803, 801, 800, 790, 784, 783, 780, 778, 774, 765, 764, 763, 761, 758, 756, 753, 750, 738, 733, 728, 725, 724, 716, 712, 711, 708, 705, 704, 701, 699, 697, 686, 685, 684, 683, 682, 680, 673, 670, 666, 663, 658, 650, 648, 645, 643, 640, 639, 634, 626, 615, 613, 603, 594, 592, 588, 584, 583, 582, 580, 579, 569, 565, 560, 559, 558, 557, 555, 547, 541, 539, 538, 534, 533, 532, 526, 520, 510, 509, 508, 505, 498, 488, 487, 485, 481, 475, 474, 472, 470, 464, 460, 456, 452, 451, 447, 446, 443, 441, 439, 432, 430, 427, 424, 415, 409, 408, 401, 398, 394, 393, 388, 386, 381, 380, 379, 376, 370, 367, 366, 362, 358, 357, 355, 354, 349, 348, 342, 337, 333, 331, 330, 324, 320, 318, 316, 312, 308, 306, 305, 304, 302, 301, 296, 291, 280, 273, 271, 270, 269, 263, 259, 258, 255, 246, 242, 239, 236, 228, 224, 223, 222, 221, 220, 213, 208, 207, 205, 203, 202, 196, 191, 190, 187, 185, 184, 180, 170, 169, 161, 160, 155, 150, 147, 141, 137, 135, 132, 130, 129, 122, 121, 117, 116, 107, 102, 96, 95, 94, 90, 89, 86, 81, 79, 78, 77, 73, 67, 61, 59, 56, 52, 49, 38, 27, 23, 19, 14, 12, 11, 4], 862, 68)
    ])
    def test(self, _, arr, target, expected_index):
        self.assertEqual(find_number(arr, target), expected_index)


def _find_pivot(arr, start, end):
    # handle bounds, not checking that the array is valid
    midpoint = (start + end)//2
    if midpoint == 0:
        return 0
    if midpoint >= len(arr) - 2:
        return len(arr) - 2

    if arr[midpoint] > arr[midpoint-1] and arr[midpoint+2] < arr[midpoint+1]:
        return midpoint
    if arr[midpoint+1] > arr[midpoint]:
        return _find_pivot(arr, midpoint+1, end)
    return _find_pivot(arr, start, midpoint-1)


def binary_search(arr, target, start, end, sign=1):
    # not present
    midpoint = (start + end)//2
    if start > end or midpoint == len(arr):
        return -1
    if arr[midpoint] == target:
        return midpoint
    if sign*arr[midpoint] < sign*target:
        return binary_search(arr, target, midpoint + 1, end, sign)
    return binary_search(arr, target, start, midpoint - 1, sign)


def find_number(arr, target):

    if len(arr) <= 2:
        return arr.index(target)

    pivot = _find_pivot(arr, 0, len(arr)-1)
    lhs_result = binary_search(arr, target, 0, pivot)
    rhs_result = binary_search(arr, target, pivot, len(arr), -1)
    if lhs_result > -1:
        return lhs_result
    if rhs_result > -1:
        return rhs_result
    return -1

