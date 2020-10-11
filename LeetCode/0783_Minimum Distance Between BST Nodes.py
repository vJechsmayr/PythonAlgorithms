# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        self.prev = float('-inf')
        self._min = float('inf')
        def inorder(root):
            if root:
                inorder(root.left)
                self._min = min(self._min, root.val-self.prev)
                self.prev = root.val
                inorder(root.right)
        inorder(root)
        return self._min
