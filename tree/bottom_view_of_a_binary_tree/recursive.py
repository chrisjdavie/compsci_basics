"""
Given a Binary Tree, we need to print the bottom view from left to right. A node x is there in output if x is the bottom most node at its horizontal distance. Horizontal distance of left child of a node x is equal to horizontal distance of x minus 1, and that of right child is horizontal distance of x plus 1. 

https://www.geeksforgeeks.org/bottom-view-binary-tree/
"""
from parameterized import parameterized
import unittest

from utils.tree import Node, TreeMaker


class Test(unittest.TestCase):

    @parameterized.expand([
        ("1 level", [(1,2,"L"), (1,3,"R")], [2, 1, 3]),
        ("LHS view", [(1,2,"L"), (2,4,"L")], [4, 2, 1]),
        ("RHS view", [(1,3,"R"), (3,7,"L")], [1, 3, 7]),
        ("Replace node", [(1,2,"L"), (2,5,"R")], [2, 5]),
        ("Same position, right most", [(1,2,"L"), (1,3,"R"), (2,5,"R"), (3,6,"L")], [2, 6, 3]),
        ("Provided example 0", [(20,8,"L"), (20,22,"R"), (8,5,"L"), (8,3,"R"), (3,10,"L"), (3,14,"R"), (22,25,"R")], [5, 10, 3, 14, 25]),
        ("Provided example 1", [(20,8,"L"), (20,22,"R"), (8,5,"L"), (8,3,"R"), (3,10,"L"), (3,14,"R"), (22,4,"L"), (22,25,"R")], [5, 10, 3, 14, 25])
    ])
    def test_trees(self, _, node_description, expected_bottom_view):
        root = TreeMaker.from_node_description(node_description)
        self.assertEqual(bottom_view(root), expected_bottom_view)

    @parameterized.expand([
        ("Null test", None, []),
        ("Single node", Node(1), [1])
    ])
    def test_corner_cases(self, _, node, expected_bottom_view):
        self.assertEqual(bottom_view(node), expected_bottom_view)


def bottom_view(root):
    return -1
