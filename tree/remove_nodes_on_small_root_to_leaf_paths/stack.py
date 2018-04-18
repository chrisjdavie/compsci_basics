"""
Given a Binary Tree and a number k, remove all nodes that lie only on root to leaf path(s) of length smaller than k.

https://www.geeksforgeeks.org/remove-nodes-root-leaf-paths-length-k/

(Clearly the recursive way is better than me doing stacks and heaps and ugly things like that,
but I figured I'd have a look at an iterative solution)
"""
from heapq import heappush, heappop
from parameterized import parameterized
import unittest

from utils.tree import TreeMaker, Node, Tree


class DpNode(Node):

    def __init__(self, data):
        self.parent = None
        self.depth = 0
        super().__init__(data)


class DpTreeMaker(TreeMaker):

    obj = DpNode

    @classmethod
    def tree_and_node_count_from_node_description(cls, node_idents):
        """This assigns parents and depths to all the nodes in the tree.

        (Stack based)
        """
        root, num_nodes = super().tree_and_node_count_from_node_description(node_idents)

        root.parent = None
        root.depth = 1

        def assign_depth_parent(parent, child, stack):
            if child:
                child.parent = parent
                child.depth = parent.depth + 1
                stack.append(child)

        stack = [root]
        while stack:
            node = stack.pop()
            assign_depth_parent(node, node.left, stack)
            assign_depth_parent(node, node.right, stack)

        return root, num_nodes


class Test(unittest.TestCase):

    @parameterized.expand([
        ("provided example 0", 
         ["0", "0L", "0R", "0LL", "0LR", "0RR", "0LLL", "0RRL"], 
         4,
         ["0", "0L", "0R", "0LL", "0RR", "0LLL", "0RRL"]),
        ("1 layer",
         ["0", "0L", "0R"],
         2,
         ["0", "0L", "0R"]),
        ("2 layers 1 removed",
         ["0", "0L", "0R", "0LL"],
         3,
         ["0", "0L", "0LL"])
    ])
    def test(self, _, node_idents, min_path_len, expected_node_idents):
        root = DpTreeMaker.from_node_idents(node_idents)
        root_produced = remove_nodes(root, min_path_len)

        root_expected = DpTreeMaker.from_node_idents(expected_node_idents)
        self.assertEqual(root_produced, root_expected)

    def test_null(self):
        min_path_len = 23
        self.assertEqual(remove_nodes(None, min_path_len), None)

    @parameterized.expand([
        ("single node", ["0"], 2),
        ("tree", ["0", "0L", "0R"], 3)
    ])
    def test_all_removed(self, _, node_idents, min_path_len):
        root = DpTreeMaker.from_node_idents(node_idents)
        root_produced = remove_nodes(root, min_path_len)
       
        self.assertEqual(root_produced, None)


def remove_nodes(root, min_path_len):
    if not root:
        return None

    stack = [root]
    # heap needed for searching each level upwards one by one.
    clean_heap = []
    
    while stack:

        node = stack.pop()
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

        if not node.left and not node.right and node.depth < min_path_len:
            heappush(clean_heap, (-node.depth, id(node), node))

    while clean_heap:
        
        node = heappop(clean_heap)[-1]

        if node == root:
            return None

        if node.parent.left == node:
            node.parent.left = None
        if node.parent.right == node:
            node.parent.right = None

        if not node.parent.left and not node.parent.right:
            heappush(clean_heap, (-node.parent.depth, id(node.parent), node.parent))

    return root
