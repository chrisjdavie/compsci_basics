"""
Given an array of numbers, return true if given array can represent preorder traversal of a Binary Search Tree, else return false. Expected time complexity is O(n).
"""
from parameterized import parameterized
import unittest


class Test(unittest.TestCase):

    @parameterized.expand([
        ("example from comments", [5, 4 ,3, 6, 8, 7, 9], True),
        ("provided example 0", [2, 4, 3], True),
        ("3 elements invalid", [2, 4, 1], False),
        ("provided example 1", [40, 30, 35, 80, 100], True),
        ("provided example 2", [40, 30, 35, 20, 80, 100], False)
    ])
    def test(self, _, arr, result_expected):
        self.assertEqual(check_represent_preorder(arr), result_expected)


class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    """Not balanced"""

    def __init__(self, root):
        self.root = root

    @classmethod
    def _insert(cls, node_old, node_new):
        if node_new.data < node_old.data:
            if node_old.left:
                cls._insert(node_old.left, node_new)
            else:
                node_old.left = node_new
        else:
            if node_old.right:
                cls._insert(node_old.right, node_new)
            else:
                node_old.right = node_new

    def insert(self, node_new):
        self._insert(self.root, node_new)

    @classmethod
    def _preorder_search(cls, node, preorder_arr):
        if not node:
            return
        
        preorder_arr.append(node.data)
        cls._preorder_search(node.left, preorder_arr)
        cls._preorder_search(node.right, preorder_arr)

    def preorder_search(self):
        preorder_arr = []
        self._preorder_search(self.root, preorder_arr)
        return preorder_arr


def check_represent_preorder(arr):
    """Working hypothesis is that if you build a search tree based on arr, and
    arr can represent a preorder search, then that search will match arr. It
    works in all the states I can think of, but I can't think of a concise 
    proof"""
    # construct binary search tree
    bst = BinarySearchTree(Node(arr[0]))
    for num in arr[1:]:
        bst.insert(Node(num))

    # return preorder search
    preorder_results = bst.preorder_search()

    # compare arrays
    return arr == preorder_results
