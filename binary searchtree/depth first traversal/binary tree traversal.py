# https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return
        
        queue = []
        queue.append(root)
        result = []
        
        while(len(queue)>0):
            new_list = []
            for _ in range(len(queue)):
                new_list.append(queue[0].val)
                node = queue.pop(0)

                if node.left is not None:
                    queue.append(node.left)

                if node.right is not None:
                    queue.append(node.right)
            result.append(new_list)
        return result
                
            
        
        