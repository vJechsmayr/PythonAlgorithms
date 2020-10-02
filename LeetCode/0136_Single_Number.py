class Solution:
    def singleNumber(self, nums):
        singleNumber = nums[0]
        for i in range(1, len(nums)):
            singleNumber = singleNumber ^ nums[i]
        return singleNumber