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


def is_subtree(root0, root1):
    comparison_root_stack = []

    # find the root of 1 in 0
    stack = [root0]
    while stack:
        
        node = stack.pop()
        if node.data == root1.data:
            comparison_root_stack.append((node, root1))
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    ret_val = False
    while comparison_root_stack:
        comparison_stack = [comparison_root_stack.pop()]
        while comparison_stack:
            node0, node1 = comparison_stack.pop()
            # continue if both are none
            if node1 is None:
                continue
            # stop if node0 is none and node1 isn't, or if the data doesn't match
            if (node0 is None and node1 is not None) or (node0.data != node1.data):
                break
            comparison_stack.append((node0.left, node1.left))
            comparison_stack.append((node0.right, node1.right))
        else:
            ret_val = True
            break
            
    return ret_val
