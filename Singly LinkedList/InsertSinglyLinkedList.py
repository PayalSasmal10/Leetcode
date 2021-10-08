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
            node = node.next
    def insertList(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == 1:
                newNode.next = None
                self.tail = newNode
            else:
                tempNode = self.head
                index=0
                while index < location-1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode


            

insersLinkedList = InsertSLinkedList()
insersLinkedList.insertList(2,1)
insersLinkedList.insertList(3,2)
insersLinkedList.insertList(4,3)
insersLinkedList.insertList(5,4)


print([node.value for node in insersLinkedList])