def nodeDepths(root):
    # Write your code here.
    nodes = [(root, 0)]
    sum_depths = 0
    while(nodes):
        node , depth = nodes.pop()
        sum_depths = sum_depths + depth
        if node.right:
            nodes.append((node.right,  depth + 1))
        if node.left:
            nodes.append((node.left, depth + 1))
    return sum_depths


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
