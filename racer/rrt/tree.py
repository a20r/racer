
class Tree(object):

    def __init__(self, value, **kwargs):
        self.children = kwargs.get("children", list())

        for child in self.children:
            child.set_parent(self)

        self.value = value
        self.parent = None

    def get_children(self):
        return self.children

    def get_value(self):
        return self.value

    def get_parent(self):
        return self.parent

    def add_child(self, child):
        child.set_parent(self)
        self.children.append(child)
        return self

    def set_value(self, val):
        self.value = val

    def set_parent(self, adult):
        self.parent = adult

    def get_path_to_root(self):
        tree_path = list()
        current_node = self
        while not current_node is None:
            current_node = current_node.get_parent()
            tree_path.append(current_node.get_value())

        return tree_path
