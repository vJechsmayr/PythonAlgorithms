# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def solve(r,k):
    x = TreeNode(k)
    ans = r
    if(not r):
        return x
    while(r and (r.left or r.right) ):
        if(r.val < k):
            if(r.right):
                r = r.right
            else:
                r.right = x
                return ans
        else:
            if(r.left):
                r = r.left
            else:
                r.left = x
                return ans
    if(r.val < k):
        r.right = x
    else:
        r.left = x
    return ans

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        return solve(root,val)
