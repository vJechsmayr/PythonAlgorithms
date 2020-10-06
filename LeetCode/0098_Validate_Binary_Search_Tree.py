# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: TreeNode, sm=[], gt=[]) -> bool:
        if root is None:
            return True
        
        if any([root.val <= x for x in sm]) or any([root.val >= x for x in gt]):
            return False
        
        return (root.left is None or self.isValidBST(root.left, sm, gt + [root.val])) and (root.right is None or self.isValidBST(root.right, sm + [root.val], gt))
