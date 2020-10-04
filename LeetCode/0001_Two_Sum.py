class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        num_of_nums = len(nums)
        i = 0
        while i < num_of_nums:
            num = target - nums[i]
            if (num in dic):
                return [dic[num], i]
            else:
                dic[nums[i]] = i
                i = i + 1



