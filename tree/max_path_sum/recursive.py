from parameterized import parameterized
import unittest


class Test(unittest.TestCase):

    @parameterized.expand([
        ( "provided example 0", [(0, 1), (1, 2), (2, 3)], [(0, 1, "L"), (0, 2, "R")], 6 ),
        ( "provided example 1", 
          [(0, 10), (1, 2), (2, 1), (3, 20), (4, 10), (5, -25), (6, 3), (7, 4)],
          [(0, 1, "L"), (0, 4, "R"), (1, 2, "L"), (1, 3, "R"), (4, 5, "R"), (5, 6, "L"), (5, 7, "R")],
          42 ),
        ( "misses root",
          [(0, 3), (1, 5), (2, 100), (3, 100), (4, 2)],
          [(0, 1, "L"), (1, 2, "L"), (1, 3, "R"), (0, 4, "R")],
          205 ),
        ( "isolated subtree",
          [(0, 5), (1, -200), (2, 100), (3, 20), (4, 15)],
          [(0, 1, "L"), (1, 2, "L"), (0, 3, "R"), (3, 4, "R")],
          100 ),
    ])
    def test(self, _, weights, joins, expected_max):
        self.assertEqual(maximum_path_sum(weights, joins), expected_max)


class Node:

    def __init__(self, ident, weight):
        self.ident = ident
        self.weight = weight
        self.left = None
        self.right = None


class Tree:

    def __init__(self, root):
        self._root = root
        self._max_overall = 0

    @classmethod
    def print_preorder(self, node):
        if not node:
            return

        print(node.ident)
        self.print_preorder(node.left)
        self.print_preorder(node.right)

    def _max_sum_path(self, node):
        if not node:
            return 0

        max_l = self._max_sum_path(node.left)
        max_r = self._max_sum_path(node.right)

        max_subtree = max([max_l + node.weight,
                           max_r + node.weight,
                           0])
        self._max_overall = max([self._max_overall,
                               max_subtree,
                               max_l + max_r + node.weight])
        return max_subtree

    def max_sum_path(self):
        self._max_sum_path(self._root)
        return self._max_overall


def construct_tree(weights, joins):

    nodes = {}    
    for ident, weight in weights:
        nodes[ident] = Node(ident, weight)

    parents = set()
    children = set()
    for parent, child, pos in joins:
        if pos == "R":
            nodes[parent].right = nodes[child]
        if pos == "L":
            nodes[parent].left = nodes[child]
        parents.add(parent)
        children.add(child)

    root = parents.difference(children).pop()
    return nodes[root]


def maximum_path_sum(weights, joins):
    root = construct_tree(weights, joins)
    tree = Tree(root)
    return tree.max_sum_path()

