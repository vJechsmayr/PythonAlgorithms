# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        myStack = []
        curr = root
        while len(myStack) or curr is not None:
            while curr is not None:
                myStack.append(curr)
                curr = curr.left
            curr = myStack.pop()
            res.append(curr.val)
            curr = curr.right            
        return res
