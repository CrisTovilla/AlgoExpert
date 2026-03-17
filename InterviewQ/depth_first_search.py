class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        # Write your code here.
        nodes = [self]
        while(nodes):
            node = nodes.pop()
            array.append(node.name)
            for child in reversed(node.children):
                nodes.append(child)
        return array
