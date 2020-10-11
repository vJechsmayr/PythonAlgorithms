import math
import sys

class Solution:
    def Find132Pattern(self, nums: List[int]):
        n = len(nums)
        top = n
        third = -sys.maxsize

        for i in range(n-1, -1 , -1):
            if nums[i] < third:
                return True
            while top < n and nums[i] > nums[top]:
                third = nums[top]
            top = top - 1
            nums[top] = nums[i]
        return False
