class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = []
        n = len(nums)
        
        def canJumpFromPosition(position, nums):
            if memo[position] != 0:
                return memo[position] == 1
            furthestJump = min(position + nums[position], n - 1)
            for i in range(position + 1, furthestJump + 1):
                if(canJumpFromPosition(i, nums)):
                    memo[position] = 1
                    return True
            memo[position] = -1
            return False
        for i in range(n):
            memo.append(0)
        memo[n - 1] = 1
        
        return canJumpFromPosition(0, nums)
