class Solution:
    def jump(self, nums):
        # n ^ 2 solution using dp
        dp = [-1 for i in range(len(nums))]
        dp[len(nums) - 1] = 0

        for i in range(len(nums)-2, -1, -1):
            step = -1
            for j in range(i + 1, min(len(nums) - 1, i + nums[i]) + 1):
                if dp[j] != -1:
                    if step == -1:
                        step = dp[j]
                    else:
                        step = min(dp[j], step)

            if step == -1:
                dp[i] = -1
            else:
                dp[i] = step + 1

        return dp[0]