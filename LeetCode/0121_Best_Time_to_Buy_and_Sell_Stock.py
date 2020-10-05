class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        if not prices:
            return ans
        
        n = len(prices)
        
        l_min = [0 for _ in range(n)]
        r_max = [0 for _ in range(n)]
        
        l_min[0] = prices[0]
        r_max[-1]= prices[-1]
        for i in range(1, n):
            l_min[i] = min(l_min[i-1], prices[i])
            r_max[n-1-i] = max(r_max[n-i], prices[n-1-i])
                
        for i in range(n-1):
            ans = max(ans, r_max[i+1] - l_min[i])
        
        return ans
