# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def middleNode_s1(linkedList):
    # Write your code here.
    nodes = []
    node = linkedList
    while node:
        nodes.append(node)
        node = node.next
    return nodes[int(len(nodes)/2)]

def middleNode_s2(linkedList):
    # Write your code here.
    twice_node = linkedList
    node = linkedList
    while twice_node and twice_node.next:
        twice_node = twice_node.next.next
        node = node.next
    return node
