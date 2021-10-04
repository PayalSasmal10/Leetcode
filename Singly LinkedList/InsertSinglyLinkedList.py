#insert an element at first

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class InsertSLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None


node1 = Node(10)
node2 = Node(20)

insersLinkedList = InsertSLinkedList()
insersLinkedList.head = node1
insersLinkedList.node.next = node2
insersLinkedList.tail = node2