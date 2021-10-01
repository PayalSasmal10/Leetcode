#create Node
class Node:
    def __init__(self, value=None):
        self.node = value
        self.next = None

#create head & tail
class SLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

node1 = Node(1)

slinkedlist = SLinkedList()

slinkedlist.head = node1
slinkedlist.head.next = node1
slinkedlist.tail = node1