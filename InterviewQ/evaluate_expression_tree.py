# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def calculateSubTree(node):
    if node.left is None and node.right is None:
        return node.value

    left_r = calculateSubTree(node.left)
    right_r = calculateSubTree(node.right)

    if node.value == -4:
        return left_r * right_r
    elif node.value == -3:
        return int(left_r / right_r)
    elif node.value == -2:
        return left_r - right_r

    return left_r + right_r
    

def evaluateExpressionTree(tree):
    # Write your code here.
    return calculateSubTree(tree)
