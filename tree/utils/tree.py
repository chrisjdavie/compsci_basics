class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


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


