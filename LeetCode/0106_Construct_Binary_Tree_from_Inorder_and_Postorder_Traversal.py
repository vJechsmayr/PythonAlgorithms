class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        return self.helperFunc(inorder, postorder, 0, len(inorder)-1, len(postorder)-1)
    def helperFunc(self, inorder: List[int], postorder: List[int], left: int, right: int, postIndex: int) -> TreeNode:
        # checks if there is node required else puts null in the binary tree
        if postIndex == -1:
            return
        # creating the root of the subtree from the value present at current postIndex
        root = TreeNode(postorder[postIndex])
        # we find the root's value in order to divide them into left and right subtree
        x = 0
        for i in range(len(inorder)):
            if root.val == inorder[i]:
                x = i
        # finding corresponding values that are roots for left and right subtrees or assign -1
        right_post = -1 if abs(right - x) == 0 else postIndex - 1
        left_post = -1 if abs(left - x) == 0 else postIndex -1 - abs(right - x)
        # calling recursively helperFunc for left and right subtrees
        root.left = self.helperFunc(inorder, postorder, left, x-1, left_post)
        root.right = self.helperFunc(inorder, postorder, x+1, right, right_post)
        return root
    