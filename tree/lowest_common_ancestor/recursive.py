"""
Given values of two values n1 and n2 in a Binary Search Tree, find the Lowest Common Ancestor (LCA). You may assume that both the values exist in the tree. 

https://www.geeksforgeeks.org/lowest-common-ancestor-in-a-binary-search-tree/
"""
from parameterized import parameterized
import unittest

from utils.tree import TreeMaker, Node, Tree

TREE_EXAMPLE = [(20, 8, "L"), (20, 22, "R"), (8, 4, "L"), (8, 12, "R"), (12, 10, "L"), (12, 14, "R")]


class Test(unittest.TestCase):

    @parameterized.expand([
        ("provided example 0",
         [(5, 4, "L"), (5, 6, "R"), (4, 3, "L"), (6, 7, "R"), (7, 8, "R")], 
         7, 8, 
         7),
        ("provided example 1",
         TREE_EXAMPLE,
         10, 14,
         12),
        ("provided example 2",
         TREE_EXAMPLE,
         14, 8,
         8),
        ("provided example 3",
         TREE_EXAMPLE,
         10, 22,
         20)
    ])
    def test(self, _, node_description, value0, value1, expected_lca_value):
        root = TreeMaker.from_node_description(node_description)
        self.assertEqual(lowest_common_ancestor(root), expected_lca_value)


def lowest_common_ancestor(root):
    return -1
