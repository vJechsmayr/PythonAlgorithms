class Solution(object):
    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        out = -1
        for i in range(len(nums)):
            if nums[~i]>=i+1:
                if i==len(nums)-1 or nums[~(i+1)]<i+1:
                    return i+1
        return out
                                                                                                                                        
