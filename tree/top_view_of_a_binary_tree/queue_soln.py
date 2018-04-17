"""
Top view of a binary tree is the set of nodes visible when the tree is viewed from the top. Given a binary tree, print the top view of it. Expected time complexity is O(n).

Note: For the problem the printing should be level wise, i.e. starting node should be root.

https://www.geeksforgeeks.org/print-nodes-top-view-binary-tree/

Similarly to the "bottom view" version of the problem, this is something of an arbitrary representation of a data structure, but we'll go with it.
"""
from parameterized import parameterized
from collections import deque
import unittest

from utils.tree import TreeMaker, Node


class Test(unittest.TestCase):

    @parameterized.expand([
        ("provided example 0", [("0", "0L", "L"), ("0", "0R", "R")], [ "0","0L", "0R"]),
        ("provided example 1", [("0", "0L", "L"), ("0", "0R", "R"), ("0L", "0LL", "L"), ("0L", "0LR", "R"), ("0R", "0RL", "L")], ["0", "0L", "0R", "0LL"]),
        ("provided example 2", [("0", "0L", "L"), ("0", "0R", "R"), ("0L", "0LL", "L"), ("0L", "0LR", "R"), ("0R", "0RL", "L"), ("0R", "0RR", "R")], ["0", "0L", "0R", "0LL", "0RR"]),
        ("provided example 3", [("0", "0L", "L"), ("0", "0R", "R"),  ("0L", "0LR", "R"), ("0LR", "0LRR", "R"), ("0LRR", "0LRRR", "R")], ["0", "0L", "0R", "0LRRR"])
    ])
    def test(self, _, node_description, expected_top_view):
        root = TreeMaker.from_node_description(node_description)
        self.assertEqual(top_view(root), expected_top_view)

    @parameterized.expand([
        ("Null tree", None, []),
        ("Single node", Node(0), [0])
    ])
    def test_corner_cases(self, _, root, expected_top_view):
        self.assertEqual(top_view(root), expected_top_view)


def top_view(root):
    """
    Solving using BFS
    """
    if not root:
        return []

    top_view_data = []
    already_seen = set()
    fifo_queue = deque([(0, root)])

    while fifo_queue:
        coords, node = fifo_queue.popleft()
        
        if coords not in already_seen:
            top_view_data.append(node.data)
            already_seen.add(coords)

        if node.left:
            fifo_queue.append((coords - 1, node.left))
        if node.right:
            fifo_queue.append((coords + 1, node.right))

    return top_view_data
