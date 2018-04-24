"""
Given two binary trees, check if the first tree is subtree of the second one. A subtree of a tree T is a tree S consisting of a node in T and all of its descendants in T. 

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
         True),
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


def _is_subtree(node0, node1):

    is_subtree_ret = []
    if not node1:
        is_subtree_ret.append(True)
    elif not node0:
        is_subtree_ret.append(False)
    else:
        is_subtree_ret.append(node0.data == node1.data)
        is_subtree_ret.append(_is_subtree(node0.left, node1.left))
        is_subtree_ret.append(_is_subtree(node0.right, node1.right))

    return all(is_subtree_ret)


def is_subtree(node0, root1):
    if not node0:
        return False

    is_subtree_ret = False
    if node0.data == root1.data:
        if _is_subtree(node0, root1):
            is_subtree_ret = True

    if not is_subtree_ret:
        is_subtree_ret = is_subtree(node0.left, root1)
    if not is_subtree_ret:
        is_subtree_ret = is_subtree(node0.right, root1)

    return is_subtree_ret
