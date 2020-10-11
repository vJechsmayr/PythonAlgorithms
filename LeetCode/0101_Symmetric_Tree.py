# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        
        return self.isMirror(root.left, root.right)
        
    
    def isMirror(self, a: TreeNode, b: TreeNode) -> bool:
        if (a and b) and (a.val == b.val):
            return self.isMirror(a.left, b.right) and self.isMirror(a.right, b.left)
            
        return a == None and b == None
