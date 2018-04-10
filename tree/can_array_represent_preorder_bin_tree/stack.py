"""
Given an array of numbers, return true if given array can represent preorder traversal of a Binary Search Tree, else return false. Expected time complexity is O(n).
"""
from parameterized import parameterized
import unittest


class Test(unittest.TestCase):

    @parameterized.expand([
        ("example from comments", [5, 4 ,3, 6, 8, 7, 9], True),
        ("provided example 0", [2, 4, 3], True),
        ("3 elements invalid", [2, 4, 1], False),
        ("provided example 1", [40, 30, 35, 80, 100], True),
        ("provided example 2", [40, 30, 35, 20, 80, 100], False)
    ])
    def test(self, _, arr, result_expected):
        self.assertEqual(check_represent_preorder(arr), result_expected)


def check_represent_preorder(arr):
    """This does solve the problem, but it's much less clear why it works
    than just building the tree and checking!"""

    can_represent = True
    stack = []
    lower_bound = -float("inf")

    for value in arr:

        if value < lower_bound:
            can_represent = False
            break
        
        while stack and stack[-1] < value:
            lower_bound = stack.pop()

        stack.append(value)

    return can_represent

