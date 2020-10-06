class Solution(object):
    def maxProfit(self, prices):
        n = len(prices)
        leftProfits = [0] * n
        rightProfits = [0] * n
        minSoFar = prices[0]
        maxSoFar = prices[-1]
        for i in range(1, n):
            leftProfits[i] = max(leftProfits[i-1], prices[i]-minSoFar)
            minSoFar = min(minSoFar, prices[i])
            
            j = n - i - 1
            rightProfits[j] = max(rightProfits[j+1], maxSoFar - prices[j])
            maxSoFar = max(maxSoFar, prices[j])
        
        maxProfit = leftProfits[n-1]
        for i in range(n-1):
            maxProfit = max(maxProfit, leftProfits[i] + rightProfits[i+1])
        return maxProfit
