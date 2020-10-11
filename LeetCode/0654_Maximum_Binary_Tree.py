class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        def helper(nums, root): 
            if not nums:
                return None
            if  nums:
                root = TreeNode(max(nums))
            ind=nums.index(max(nums))
            root.left= helper(nums[:ind],root)
            root.right=helper(nums[ind+1:],root)
            return root
        root=TreeNode(0)
        return helper(nums,root)
