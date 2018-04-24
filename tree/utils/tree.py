class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __eq__(self, other):

        try:
            return self.data == other.data and self.left == other.left and self.right == other.right
        except AttributeError:
            return False

    def __repr__(self):
        return "Node(data:{})".format(self.data)


class Tree:

    @classmethod
    def print_two_trees(cls, tree0, tree1):
        if tree0:
            print([tree0, tree0.left, tree0.right], end=" ")
        else:
            print("Null tree0", end=" ")
        if tree1:
            print([tree1, tree1.left, tree1.right])
        else:
            print("Null tree1")

        if tree0 and tree1:
            cls.print_two_trees(tree0.left, tree1.left)
            cls.print_two_trees(tree0.right, tree1.right)


class TreeMaker:

    obj = Node

    @classmethod
    def from_node_description(cls, node_description):
        return cls.tree_and_node_count_from_node_description(node_description)[0]

    @classmethod
    def tree_and_node_count_from_node_description(cls, node_description):
        nodes = {}
        children_data = set()
        parents_data = set()
        for data_parent, data_child, side in node_description:
            if data_parent not in nodes:
                nodes[data_parent] = cls.obj(data_parent)
                parents_data.add(data_parent)
            parent = nodes[data_parent]

            if data_child not in nodes:
                nodes[data_child] = cls.obj(data_child)
                children_data.add(data_child)
            child = nodes[data_child]

            if side == "L":
                parent.left = child
            if side == "R":
                parent.right = child
        data_root = parents_data.difference(children_data).pop()
	
        return nodes[data_root], len(parents_data.union(children_data))

    @classmethod
    def from_node_idents(cls, node_idents):
        if len(node_idents) == 1:
            return cls.obj(node_idents[0])

        node_description = [ (ident[:-1], ident, ident[-1]) for ident in node_idents[1:] ]
        return cls.from_node_description(node_description)
