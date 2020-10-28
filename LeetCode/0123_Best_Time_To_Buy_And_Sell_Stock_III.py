
'''
	Python program to solve issue: 0123- Best Time to Buy adn Sell Stock

	Issue Id: #383
'''


class Solution:
 
	#Evalutes the all days to buy and sell stock & Generate maximum profit
    def maxProfit(self, prices: List[int]) -> int:

    	#Checks whether price array is empty or less then 2 elements
        if prices==None or len(prices) < 2:
            return 0

        maxProfit=0  #Stores maximum profit

        minPrice=prices[0]  #the minimum price from the first day to day k-1

        #the maximum profit with at most one transaction from the first day to day k
        first=[0 for x in range(0,len(prices))]

        #Evaluates maximum profit from first day to last day
        for i in range(1,len(prices)):
            maxProfit= max(maxProfit, prices[i]- minPrice)
            first[i]= maxProfit
            minPrice= min(minPrice, prices[i])

        maxProfit=0
        maxPrice=prices[len(prices)-1] #the maximum price from day k+1 to the last day

        #the maximum profit with at most one transaction from day k to the last day
        second=[0 for x in range(len(prices))]
		
		#Evaluates maximum profit from last day to first day
        for j in range(len(prices)-2,-1,-1):
            maxProfit = max(maxProfit, (maxPrice - prices[j]))
            second[j] = int(maxProfit)
            maxPrice = max(maxPrice, prices[j])
			
        maxProfit=0

        #Evaluates maximum profit for all days with at most TWO transaction
        for k in range(0,len(prices)):
            maxProfit= max(maxProfit, first[k]+second[k])
		
        return maxProfit