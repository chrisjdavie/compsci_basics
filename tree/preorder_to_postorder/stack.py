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
         [1, 3, 2, 4]),
        ("lhs and rhs behaviour",
         [40, 20, 25, 22, 21, 30, 35, 50],
         [21, 22, 35, 30, 25, 20, 50, 40])
    ])
    def test(self, _, preorder_arr, postorder_arr):
        self.assertEqual(list(preorder_to_postorder(preorder_arr)), 
                         postorder_arr)


def preorder_to_postorder(preorder):

    value_stack = []
    root_stack = []
    postorder = []

    for val in preorder:
        if value_stack and value_stack[-1] > val:
            root_stack.append(value_stack[-1])

        while (root_stack and val > root_stack[-1] 
               and value_stack and value_stack[-1] < root_stack[-1]):
            postorder.append(value_stack.pop())
            if value_stack[-1] == root_stack[-1]:
                root_stack.pop()

        value_stack.append(val)

    while value_stack:
        postorder.append(value_stack.pop())

    return postorder
