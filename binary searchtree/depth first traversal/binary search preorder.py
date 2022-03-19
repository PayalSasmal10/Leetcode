#https://leetcode.com/problems/binary-tree-preorder-traversal/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode):
        self.result = []
        def Preorder(node):
            if node == None:
                return
            self.result.append(node.val)
            Preorder(node.left)
            Preorder(node.right)
        
        Preorder(root)
        return self.result
        