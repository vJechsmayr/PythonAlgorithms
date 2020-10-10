# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    count = 0
    past_sums = {}

    def pathSum(self, root: TreeNode, sum: int) -> int:
        if root is not None:
            self.recurse(root, 0, sum)
        return self.count

    def recurse(self, node, summed, target):
        if node is None:
            return False
        else:
            summed += node.val
            if summed == target:
                self.count += 1
            if summed - target in self.past_sums:
                self.count += self.past_sums[summed - target]
            if summed in self.past_sums:
                self.past_sums[summed] += 1
            else:
                self.past_sums[summed] = 1   
            self.recurse(node.left, summed, target)
            self.recurse(node.right, summed, target)
            self.past_sums[summed] -= 1
