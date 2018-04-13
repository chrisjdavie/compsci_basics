"""
Given an array representing preorder traversal of BST, print its postorder traversal. 
"""
from parameterized import parameterized
import unittest


# TODO - check that it's a valid binary search tree


class Test(unittest.TestCase):

    @parameterized.expand([
        ("lhs only",
         [3, 2, 1],
         [1, 2, 3]),
        ("rhs only",
         [1, 2, 3],
         [3, 2, 1]),
        ("1 layer",
         [2, 1, 3],
         [1, 3, 2]),
        ("rhs subtree",
         [1, 3, 2, 4],
         [2, 4, 3, 1]),
        ("provided example 0",
         [40, 30, 35, 80, 100], 
         [35, 30, 100, 80, 40]),
        ("provided example 1",
         [40, 30, 32, 35, 80, 90, 100 ,120],
         [35, 32, 30, 120, 100, 90, 80, 40]),
        ("my example",
         [5, 4, 3, 6, 8, 7, 9],
         [3, 4, 7, 9, 8, 6, 5]),
        ("failed test 0",
         [4, 2, 1, 3],
         [1, 3, 2, 4])
    ])
    def test(self, _, preorder_arr, postorder_arr):
        self.assertEqual(list(preorder_to_postorder(preorder_arr)), 
                         postorder_arr)


def preorder_to_postorder(arr):

    current_root = -float("inf")
    stack = []

    for val in arr:

        while stack and val > current_root and stack[-1] < current_root:
            yield stack.pop()

        stack.append(val)

        if val > current_root:
            current_root = val

    while stack:
        yield stack.pop()
