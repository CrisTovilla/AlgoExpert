def findClosestValueInBst(tree, target):
    # Write your code here.
    node = tree
    closest = node.value
    difference = abs(node.value - target)
    while(node):
        value = node.value
        if abs(value - target) < difference:
            difference = abs(value - target)
            closest = value
        if value > target:
            node = node.left
        elif value < target:
            node = node.right
        else:
            break
    return closest
        
        
        


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
