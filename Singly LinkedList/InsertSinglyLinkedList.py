#insert an element at first

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class InsertSLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def insertList(self, prv, value, location):
        newNode = Node(value)
        if location == 0:
            newNode.next = self.head
            self.head = newNode
        elif location == -1:
            newNode.next = None
            self.tail = newNode
        else:
            newNode.next = prv.next
            

            

insersLinkedList = InsertSLinkedList()
insersLinkedList.head = node1
insersLinkedList.tail = node2