# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        q = []
        t = []
        
        if root:
            q.append((0, root))
        
        while len(q) > 0:
            level, curr = q.pop(0)
            
            if level >= len(t):
                t.append([])
            t[level].append(curr.val)
            
            if curr.left:
                q.append((level + 1, curr.left))
            if curr.right:
                q.append((level + 1, curr.right))
        
        return reversed(t)
