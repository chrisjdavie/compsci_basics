"""
Given a Binary Tree and a number k, remove all nodes that lie only on root to leaf path(s) of length smaller than k.

https://www.geeksforgeeks.org/remove-nodes-root-leaf-paths-length-k/
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
        ("1 layer",
         ["0", "0L", "0R"],
         2,
         ["0", "0L", "0R"]),
        ("2 layers 1 removed",
         ["0", "0L", "0R", "0LL"],
         3,
         ["0", "0L", "0LL"])
    ])
    def test(self, _, node_idents, min_path_len, expected_node_idents):
        root = TreeMaker.from_node_idents(node_idents)
        root_produced = remove_nodes(root, min_path_len)

        root_expected = TreeMaker.from_node_idents(expected_node_idents)
        self.assertEqual(root_produced, root_expected)

    def test_null(self):
        min_path_len = 23
        self.assertEqual(remove_nodes(None, min_path_len), None)

    @parameterized.expand([
        ("single node", ["0"], 2),
        ("tree", ["0", "0L", "0R"], 3)
    ])
    def test_all_removed(self, _, node_idents, min_path_len):
        root = TreeMaker.from_node_idents(node_idents)
        root_produced = remove_nodes(root, min_path_len)
       
        self.assertEqual(root_produced, None)


def remove_nodes(node, min_path_len, depth=1):
    if not node:
        return None

    node.left = remove_nodes(node.left, min_path_len, depth + 1)
    node.right = remove_nodes(node.right, min_path_len, depth + 1)

    if not node.left and not node.right and depth < min_path_len:
        return None

    return node
