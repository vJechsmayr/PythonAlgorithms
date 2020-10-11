class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        profit = 0
        mincost = prices[0]
        
        for i in range(1, len(prices)):
            profit = max(profit, prices[i] - mincost)
            mincost = min(mincost, prices[i])
        return profit