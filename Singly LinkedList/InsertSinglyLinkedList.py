#insert an element at first

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class InsertSLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            

insersLinkedList = InsertSLinkedList()
insersLinkedList.head = node1
insersLinkedList.tail = node2