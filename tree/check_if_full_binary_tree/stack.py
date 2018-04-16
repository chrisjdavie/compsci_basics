"""
Check whether a binary tree is a full binary tree or not

A full binary tree is defined as a binary tree in which all nodes have either zero or two child nodes. Conversely, there is no node in a full binary tree, which has one child node.

https://www.geeksforgeeks.org/check-whether-binary-tree-full-binary-tree-not/

Strictly, I don't need to build a tree for this, but will do anyways
"""
from parameterized import parameterized
import unittest

from .tree import Node, TreeMaker


class Test(unittest.TestCase):
    
    @parameterized.expand([
        ("Single level full", [(1,2,"L"), (1,3,"R")], True),
        ("Single level not full", [(1,2,"L")], False),
        ("provided example 0", [(1,2,"L"), (1,3,"R"), (2,4,"L"), (2,5,"R")], True),
        ("provided example 1", [(1,2,"L"), (1,3,"R"), (2,4,"L")], False)
    ])
    def test_trees(self, _, node_description, is_full_expected):
        root = TreeMaker.from_node_description(node_description)
        self.assertEqual(is_full_binary_tree(root), is_full_expected)

    @parameterized.expand([
        ("Null test", None, True),
        ("Single node", Node(0), True)
    ])
    def test_corner_cases(self, _, root, is_full_expected):
        self.assertEqual(is_full_binary_tree(root), is_full_expected)


def is_full_binary_tree(root):
    if root is None:
        return True

    stack = [root]
    is_full_bt = True

    while stack:
        node = stack.pop()
        if bool(node.left) ^ bool(node.right):
            is_full_bt = False
            break
        if node.left:
            stack.append(node.left)
            stack.append(node.right)

    return is_full_bt

