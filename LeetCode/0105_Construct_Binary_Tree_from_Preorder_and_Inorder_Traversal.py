# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        
        n = preorder.pop(0)
        i = inorder.index(n)
        
        l = self.buildTree(preorder[:i], inorder[:i])
        r = self.buildTree(preorder[i:], inorder[i+1:])
        
        return TreeNode(n, l, r)

