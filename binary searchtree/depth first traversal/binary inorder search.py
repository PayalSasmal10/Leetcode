# https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def inorderTraversal(self, root: TreeNode):
        self.test = []
        def Inorder(node):
            
            if node == None:
                return
            
            Inorder(node.left)
            self.test.append(node.val)
            Inorder(node.right)
        
        Inorder(root)
        
        return self.test
        
        