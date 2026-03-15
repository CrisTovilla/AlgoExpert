# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    

def branchSums(root):
    # Write your code here.
    nodes = [(root, 0)]
    results = []
    while(nodes):
        node, sum = nodes.pop()

        if node.left is None and node.right is None:
            results.append(sum + node.value)
        
        if node.right:
            nodes.append((node.right, sum + node.value))
        if node.left:
            nodes.append((node.left, sum + node.value))
    return results
