# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root == None:
            return
        
        queue = []
        queue.append(root)
        result = []
        
        while(len(queue)>0):
            summ = 0
            length =  len(queue)
            for _ in range(len(queue)):
                node = queue.pop(0)
                summ += node.val
                
                if node.left is not None:
                    queue.append(node.left)
                    
                if node.right is not None:
                    queue.append(node.right)
            result.append(summ/length)
        return result
       
            
                
            