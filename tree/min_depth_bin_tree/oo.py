"""
Given a binary tree, find its minimum depth. The minimum depth is the number of nodes along the shortest path from root node down to the nearest leaf node.

https://www.geeksforgeeks.org/find-minimum-depth-of-a-binary-tree/
"""
from collections import deque
from parameterized import parameterized
import unittest


class Test(unittest.TestCase):

    @parameterized.expand([
        ("1 2 R 1 3 L", 2),
        ("10 20 L 10 30 R 20 40 L 20 60 R", 2)
    ])
    def test(self, tree_str, expected_min_depth):
        root = min_depth_from_str(tree_str)
        self.assertEqual(min_depth_bin_tree(root), expected_min_depth)


class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return self.id


class NodeTools:

    @staticmethod
    def set_child(node, child, pos):
        if pos == "L":
            node.left = child
        else:
            node.right = child

    @classmethod
    def has_children(cls, node):
        return bool(cls.get_children(node))

    @staticmethod
    def get_children(node):
        if node.left and node.right:
            return [node.left, node.right]
        if node.left:
            return [node.left]
        if node.right:
            return [node.right]
        return []


def min_depth_from_str(tree_str):

    # construct tree
    tree = {}
    children = set()
    parents = set()
    for parent, child, pos in zip(*[iter(tree_str.strip().split())]*3):
        if parent not in tree:
            tree[parent] = Node(parent)
            parents.add(parent)
        if child not in tree:
            tree[child] = Node(child)
            children.add(child)
        NodeTools.set_child(tree[parent], tree[child], pos)

    root = parents.difference(children).pop()

    return tree[root]


def min_depth_bin_tree(root):

    explore = deque([(1, root)])

    while explore:
        depth, node = explore.popleft()
        
        if not NodeTools.has_children(node):
            return depth
        for node in NodeTools.get_children(node):
            explore.append((depth + 1, node))

