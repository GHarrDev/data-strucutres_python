class TreeNode:
    def __init__(self, name, position):
        self.children = []
        self.parent = None
        self.name = name
        self.position = position

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
           level += 1
           p= p.parent
        return level

    def print_tree(self, type, level = None):
        spaces = " " * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""        
        if type == "name":
            print(prefix + self.name)
        elif type == "position":
            print(prefix + self.position)
        elif type == "both":
            print(prefix + self.name, self.position)
        else:
            raise ValueError("Valid arguements are 'name', 'position' or 'both'.")

        if self.children:
            for child in self.children:
                child.print_tree(type)

