class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        used=[]
        for x in nums:
            if nums.count(x)==1:
                return x
