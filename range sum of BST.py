# https://leetcode.com/problems/range-sum-of-bst/submissions/

# took 450ms - need to reduce

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        result = []
        summ = 0
        
        def inorder(root):
            if root == None:
                return
                
            inorder(root.left)
            result.append(root.val)
            inorder(root.right)
        inorder(root)
        
        for i in result:
            if i >= low and i<=high:
                summ += i
        return summ
                

        
