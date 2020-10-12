class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        self.ans=[]
        def preorder(root):
            if root is None:
                return
            self.ans.append(root.val)
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return self.ans