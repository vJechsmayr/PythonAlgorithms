class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(0, len(nums)):
            soln = 0
            for j in range(0, len(nums)):
                if(nums[j] < nums[i] and j != i):
                    soln += 1
            ans. append(soln)
        return ans