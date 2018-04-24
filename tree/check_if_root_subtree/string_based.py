"""
Given two binary trees, check if a second tree S consists of a node in the first tree T and all of its descendants in T, and also includes the nulls in the second tree.

https://www.geeksforgeeks.org/check-binary-tree-subtree-another-binary-tree-set-2/
"""
from parameterized import parameterized
import unittest

from utils.tree import TreeMaker, Node

EXAMPLE_TREE = [(26, 10, "L"), (10, 20, "L"), (10, 30, "R"), (20, 40, "L"), (20, 60, "R")]



class Test(unittest.TestCase):

    @parameterized.expand([
        ("provided example 0", 
         [("z", "x", "L"), ("z", "e", "R"), ("e", "k", "R"), ("x", "a", "L"), ("x", "b", "R"), ("a", "c", "R")],
         [("x", "a", "L"), ("x", "b", "R"), ("a", "c", "R")],
         True),
        ("provided example 1",
         EXAMPLE_TREE,
         EXAMPLE_TREE,
         True),
        ("missing_node",
         [(2, 1, "R")],
         [(1, 4, "R")],
         False),
        ("different data",
         [(2, 1, "R"), (1, 3, "R")],
         [(1, 4, "R")],
         False),
        ("nested tree",
         [(2, 1, "R"), (1, 7, "L"), (1, 3, "R"), (3, 6, "L"), (3, 5, "R")],
         [(1, 3, "R")],
         False),
        ("identical trees",
         [(1, 3, "R")],
         [(1, 3, "R")],
         True),
        ("root not in tree",
         [(1, 3, "R")],
         [(5, 3, "R")],
         False),
        ("failed test 0",
         [(20, 10, "L"), (10, 5, "L"), (5, 2, "L"), (2, 3, "R")],
         [(20, 10, "L"), (10, 5, "L"), (5, 2, "L"), (2, 3, "R"), (20, 30, "R"), (30, 15, "L")],
         False)
    ])
    def test(self, _, node_des0, node_des1, is_subtree_expected):
        root0 = TreeMaker.from_node_description(node_des0)
        root1 = TreeMaker.from_node_description(node_des1)
        self.assertEqual(is_subtree(root0, root1), is_subtree_expected)

    def test_provided_example_2(self):
        """Can't use other methods as this has a duplicated node data in it"""        
        root0 = Node(26)
        root0.left = Node(10)
        root0.right = Node(3)
        root0.right.right = Node(3)
        root0.left.left = Node(4)
        root0.left.right = Node(6)
        root0.left.right.left = Node(30)
        node_des1 = [(10, 4, "L"), (10, 6, "R"), (4, 30, "R")]
        root1 = TreeMaker.from_node_description(node_des1)

        is_subtree_expected = False
        self.assertEqual(is_subtree(root0, root1), is_subtree_expected)

    def test_tree_with_duplicate_data(self):
        root0 = Node(3)
        root0.left = Node(3)
        root0.left.right = Node(1)
        root1 = Node(3)
        root1.right = Node(1)

        is_subtree_expected = True
        self.assertEqual(is_subtree(root0, root1), is_subtree_expected)


def preorder(node, preorder_data=None):
    if not node:
        return []
    if preorder_data is None:
        preorder_data = []

    preorder_data.append(node.data)
    preorder(node.left, preorder_data)
    preorder(node.right, preorder_data)
    
    return preorder_data


def inorder(node, inorder_data=None):
    if not node:
        return []
    if inorder_data is None:
        inorder_data = []

    preorder(node.left, inorder_data)
    inorder_data.append(str(node.data))
    preorder(node.right, inorder_data)

    return inorder_data


def arr_to_str(arr):
    return "".join([ str(data) for data in arr ])


def is_subtree(root0, root1):
    
    def string_index(root0, root1, order_func):

        str0 = arr_to_str(order_func(root0))
        str1 = arr_to_str(order_func(root1))
        
        return str0.find(str1)

    if (check_tree_present(root0, root1, preorder) == -1
            or check_tree_present(root0, root1, inorder) == -1):
        return False

    return True
