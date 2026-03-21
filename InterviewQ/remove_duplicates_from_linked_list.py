# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    # Write your code here.
    node = linkedList
    while node :
        next_distinct_node = node.next
        while next_distinct_node and next_distinct_node.value == node.value:
            next_distinct_node = next_distinct_node.next
        node.next = next_distinct_node
        node = node.next
    return linkedList
