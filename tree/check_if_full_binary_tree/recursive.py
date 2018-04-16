from parameterized import parameterized
import unittest

from utils.tree import Node, TreeMaker


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


def is_full_binary_tree(node):
    if node is None:
        return True

    if (bool(node.left) ^ bool(node.right)):
        return False

    return is_full_binary_tree(node.left) and is_full_binary_tree(node.right)

