"""
Given values of two values n1 and n2 in a Binary Search Tree, find the Lowest Common Ancestor (LCA). You may assume that both the values exist in the tree. 

https://www.geeksforgeeks.org/lowest-common-ancestor-in-a-binary-search-tree/

This is my first go at this task - it worked, but looking at the provided
solution, I didn't use that it's a binary search tree, which would be 
worst case O(logN), I searched the whole tree, which is O(N).
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
         20),
        ("2 nodes",
         [(20, 8, "L")],
         20, 8,
         20)
    ])
    def test(self, _, node_description, value0, value1, expected_lca_value):
        root = TreeMaker.from_node_description(node_description)
        self.assertEqual(lowest_common_ancestor(root, value0, value1), expected_lca_value)


def _lowest_common_ancestor(node, value0, value1):
    if node is None:
        return False, False, None

    val0_in_left, val1_in_left, lca_val_left = _lowest_common_ancestor(
        node.left, value0, value1)
    val0_in_right, val1_in_right, lca_val_right = _lowest_common_ancestor(
        node.right, value0, value1)

    val0_in_subtree = (val0_in_right or val0_in_left or value0 == node.data)
    val1_in_subtree = (val1_in_right or val1_in_left or value1 == node.data)

    lca_val = None
    if lca_val_left:
        lca_val = lca_val_left
    elif lca_val_right:
        lca_val = lca_val_right
    elif val0_in_subtree and val1_in_subtree:
        lca_val = node.data

    return val0_in_subtree, val1_in_subtree, lca_val


def lowest_common_ancestor(root, value0, value1):
    return _lowest_common_ancestor(root, value0, value1)[-1]
