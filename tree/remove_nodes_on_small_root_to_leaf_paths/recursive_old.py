"""
Given a Binary Tree and a number k, remove all nodes that lie only on root to leaf path(s) of length smaller than k.

https://www.geeksforgeeks.org/remove-nodes-root-leaf-paths-length-k/

**Notes**
This solution works after a fashion, but it's odd for trees that ought to disappear - as I'm
checking the original node for a tree, it cannot be replaced with null (well, I could, but not
sensibly). The provided solution was much more consistent and better than mine, so I updated it.
"""
from parameterized import parameterized
import unittest

from utils.tree import TreeMaker, Node, Tree


class Test(unittest.TestCase):

    @parameterized.expand([
        ("provided example 0", 
         ["0", "0L", "0R", "0LL", "0LR", "0RR", "0LLL", "0RRL"], 
         4,
         ["0", "0L", "0R", "0LL", "0RR", "0LLL", "0RRL"]),
        ("single node",
         ["0"],
         0,
         ["0"]),
        ("1 layer",
         ["0", "0L", "0R"],
         2,
         ["0", "0L", "0R"]),
        ("1 layer all removed",
         ["0", "0L", "0R"],
         3,
         ["0"]),
        ("2 layers 1 removed",
         ["0", "0L", "0R", "0LL"],
         3,
         ["0", "0L", "0LL"])
    ])
    def test(self, _, node_idents, min_path_len, expected_node_idents):
        root = TreeMaker.from_node_idents(node_idents)
        remove_nodes(root, min_path_len)

        root_expected = TreeMaker.from_node_idents(expected_node_idents)
        self.assertEqual(root, root_expected)

    def test_null(self):
        min_path_len = 23
        remove_nodes(None, min_path_len)

    def test_single_node(self):
        root = Node(0)
        remove_nodes(root, 0)

        expected_root = Node(0)        
        self.assertEqual(root, expected_root)


def remove_nodes(node, min_path_len, path_len=0):
    if not node:
        return path_len

    left_path_len = remove_nodes(node.left, min_path_len, path_len + 1)
    if left_path_len < min_path_len:
        node.left = None

    right_path_len = remove_nodes(node.right, min_path_len, path_len + 1)
    if right_path_len < min_path_len:
        node.right = None

    return max([left_path_len, right_path_len])
