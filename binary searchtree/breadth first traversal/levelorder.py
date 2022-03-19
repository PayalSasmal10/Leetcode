from unittest import result


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

    def buildTree(self,data):
        if data == self.data:
            return
        
        elif data < self.data:
            if self.left:
                self.left.buildTree(data)
            else:
                self.left = Node(data)

        else:
            if self.right:
                self.right.buildTree(data)
            else:
                self.right = Node(data)
    
    def levelOrder(root):
        if root == None:
            return

        queue = []
        queue.append(root)
        result = []
        summ = 0

        while(len(queue)>0):
            new_list = []
            for _ in range(len(queue)):
                new_list.append(queue[0].data)
                node = queue.pop(0)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
                
            result.append(new_list)
        j = len(result)-1
        print(len(result[j]))      
        for k in range(len(result[j])):
            summ += result[j][k]

        return summ
            

        
s = Node(10)
s.buildTree(8)
s.buildTree(5)
s.buildTree(4)
s.buildTree(7)
s.buildTree(12)
s.buildTree(11)
s.buildTree(17)
print(s.levelOrder())
# print(s.addHighestLeafNode())

"""

            ‌1‌0 ‌
           ‌/‌  ‌\‌ ‌
         ‌8     ‌12‌ ‌
        ‌/‌  ‌   /  \
       ‌5   ‌  11   17
      / \
     4   7 
"""
