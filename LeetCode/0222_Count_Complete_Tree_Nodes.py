# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        
        if root == None: return 0
        right, left = root, root
        h_l , h_r = 0, 0

        while left != None:
            h_l +=1
            left = left.left

        while right != None:
            h_r +=1
            right = right.right


        if (h_l == h_r) : return(1 << h_l) -1

        return 1+ self.countNodes(root.left) + self.countNodes(root.right)
