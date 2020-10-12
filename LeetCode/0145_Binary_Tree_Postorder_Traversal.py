class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        postorder = []
        s = []
        v = set()
        if root:
            s.append(root)
        while s:
            r = s[-1]
            if r not in v:
                if r.right:
                    s.append(r.right)
                    v.add(r)

                if r.left:
                    s.append(r.left)
                    v.add(r)

                if r.right is None and r.left is None:
                    r = s.pop()
                    postorder.append(r.val)
            else:
                r = s.pop()
                postorder.append(r.val)

        return postorder