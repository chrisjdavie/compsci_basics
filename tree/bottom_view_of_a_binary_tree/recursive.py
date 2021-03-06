"""
Given a Binary Tree, we need to print the bottom view from left to right. A node x is there in output if x is the bottom most node at its horizontal distance. Horizontal distance of left child of a node x is equal to horizontal distance of x minus 1, and that of right child is horizontal distance of x plus 1. 

https://www.geeksforgeeks.org/bottom-view-binary-tree/

This is all a bit arbitrary, assumes some sort of x & y coordinates for what is, in essence, and abstract data type. But when in Rome...
"""
from parameterized import parameterized
import unittest

from utils.tree import Node, TreeMaker

from .bottom_view import BottomViewData


class Test(unittest.TestCase):

    @parameterized.expand([
        ("1 level", [(1,2,"L"), (1,3,"R")], [2, 1, 3]),
        ("LHS view", [(1,2,"L"), (2,4,"L")], [4, 2, 1]),
        ("RHS view", [(1,3,"R"), (3,7,"R")], [1, 3, 7]),
        ("Replace node", [(1,2,"L"), (2,5,"R")], [2, 5]),
        ("Same position, right most", [(1,2,"L"), (1,3,"R"), (2,5,"R"), (3,6,"L")], [2, 6, 3]),
        ("Depth beats order", [("0","0L","L"), ("0","0R","R"), ("0L","0LR","R"), ("0LR","0LRR","R")],
["0L", "0LR", "0LRR"]),
        ("Provided example 0", [(20,8,"L"), (20,22,"R"), (8,5,"L"), (8,3,"R"), (3,10,"L"), (3,14,"R"), (22,25,"R")], [5, 10, 3, 14, 25]),
        ("Provided example 1", [(20,8,"L"), (20,22,"R"), (8,5,"L"), (8,3,"R"), (3,10,"L"), (3,14,"R"), (22,4,"L"), (22,25,"R")], [5, 10, 4, 14, 25])
    ])
    def test_trees(self, _, node_description, expected_bottom_view):
        root, num_nodes = TreeMaker.tree_and_node_count_from_node_description(node_description)
        self.assertEqual(bottom_view(root, num_nodes), expected_bottom_view)

    @parameterized.expand([
        ("Null test", None, []),
        ("Single node", Node(1), [1])
    ])
    def test_corner_cases(self, _, node, expected_bottom_view):
        self.assertEqual(bottom_view(node, 1), expected_bottom_view)


def _bottom_view(node, x_coord, depth, bottom_view_data):
    if not node:
        return

    bottom_view_data[x_coord] = (depth, node.data)

    _bottom_view(node.left, x_coord - 1, depth + 1, bottom_view_data)
    _bottom_view(node.right, x_coord + 1, depth + 1, bottom_view_data)


def bottom_view(root, num_nodes):
    """Using a dict here is worst-case less quick than using an empty array 
    (you'd need to sort the dict indicies).

    A dict feels more Pythonic, and in the general case is probably as fast with
    less code. In real life I'd use a dict, but these tests op"""

    bottom_view_data = BottomViewData(num_nodes)

    _bottom_view(root, 0, 0, bottom_view_data)

    return bottom_view_data.view()
