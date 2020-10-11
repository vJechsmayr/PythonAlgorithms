def solve(n):
    dp = [0]*(n+1)
    offset = 1
    for i in range(1,n+1):
        if(not i&(i-1)):
            offset = i
        dp[i] = dp[i-offset] + 1
    return dp

class Solution:
    def countBits(self, num: int) -> List[int]:
        return solve(num)
