from string import ascii_letters
from itertools import cycle, tee, chain, accumulate, count, islice
from parameterized import parameterized
from string import ascii_letters
import unittest
from queue import LifoQueue, Queue

from utils.tree import TreeMaker, Node, Tree
"""
Given a Perfect Binary Tree, reverse the alternate level nodes of the binary tree. 

Given tree: 
               a
            /     \
           b       c
         /  \     /  \
        d    e    f    g
       / \  / \  / \  / \
       h  i j  k l  m  n  o 

Modified tree:
  	           a
            /     \
           c       b
         /  \     /  \
        d    e    f    g
       / \  / \  / \  / \
      o  n m  l k  j  i  h 

https://www.geeksforgeeks.org/reverse-alternate-levels-binary-tree/
"""

def character_iterator(switch=False):
    """
    Returns a BFS representation of the trees above.

    If not switch, produces "Given", if switch, produces "Modified"
    """
    this, p1 = tee(chain([0],accumulate([2**i for i in range(1000)])))
    next(p1)
    for level, i_l0, i_r0 in zip(count(), this, p1):
        i_l, i_r, di = i_l0, i_r0, 1
        if switch and level%2:
            i_l, i_r, di = i_r-1, i_l-1, -1
        for lett in ascii_letters[i_l:i_r:di]:
            yield(lett)


def build_node_descr(levels, switch=False):
    """
    Produces a node description of the above binary trees
    """
    num_parents = sum([2**i for i in range(levels-1)])
    parents, children = tee(character_iterator(switch))
    next(children)
    node_descr = []
    for parent_ident in islice(parents, num_parents):
        node_descr.append((parent_ident, next(children), "L"))
        node_descr.append((parent_ident, next(children), "R"))
    return node_descr


class Test(unittest.TestCase):

    @parameterized.expand([
        (2,), (3,), (4,)
    ])
    def test(self, levels):
        node_descr = build_node_descr(levels)
        node_descr_expected = build_node_descr(levels, True)
        
        root = TreeMaker.from_node_description(node_descr)
        root_expected = TreeMaker.from_node_description(node_descr_expected)

        reverse_tree(root)
        self.assertEqual(root, root_expected)


    def test_single_node(self):
        root = Node("a")
        root_expected = Node("a")

        reverse_tree(root)

        self.assertEqual(root, root_expected)


    def test_null(self):
        reverse_tree(None)


def _reverse_tree(node_lhs, node_rhs, depth):
    if not node_lhs:
        return

    if depth%2:
        node_lhs.data, node_rhs.data = node_rhs.data, node_lhs.data

    _reverse_tree(node_lhs.left, node_rhs.right, depth + 1)
    _reverse_tree(node_lhs.right, node_rhs.left, depth + 1)


def reverse_tree(root):
    if not root or not root.left:
        return

    _reverse_tree(root.left, root.right, 1)
