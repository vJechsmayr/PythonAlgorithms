class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        R, C = len(dungeon), len(dungeon[0])
        hi = [sum([r for r in row if r<0]+[0]) for row in dungeon]
        if not hi:return 1
        else: hi = sum(hi)
        lo, hi = 1, -hi+1
        
        def dp(mid):
            dp = [[-float('inf')]*(C+1) for _ in range(R+1)]
            dp[1][1] = mid + dungeon[0][0]
            if dp[1][1]<=0:return False
            for i in range(1, R+1):
                for j in range(1, C+1):
                    this_val = max(dp[i][j-1], dp[i-1][j])+dungeon[i-1][j-1]
                    if this_val > 0:dp[i][j] = this_val
            return dp[R][C]>0 
                                 
        while lo < hi:
            mid = (lo+hi)//2
            if dp(mid):
                hi = mid
            else:
                lo = mid+1
        return lo
