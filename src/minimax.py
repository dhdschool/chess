class Node:
    def __init__(self, score, parent=None):
        self.score = score
        if parent is None:
            self.depth = 0
        else:
            self.depth = self.parent.depth + 1
        self.children = []
    
    def add_child(self, node):
        self.children.append(node)
