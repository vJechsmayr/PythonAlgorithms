class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        def traverse(root):
            if not root: return
            ret.append(root.val)
            for child in root.children:
                traverse(child)

        ret = []
        traverse(root)
        return ret
