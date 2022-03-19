# https://leetcode.com/problems/binary-tree-postorder-traversal/submissions/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode):
        result = []
        
        def inorder(root):
            if root == None:
                return
            
            inorder(root.left)
            inorder(root.right)
            result.append(root.val)
            
        inorder(root)
        return result
        
