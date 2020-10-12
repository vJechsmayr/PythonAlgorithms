class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        newBoltes=numBottles
        sum1=0
        sum1=numBottles
        
        while numBottles>=numExchange:
            newBoltes=numBottles//numExchange
            sum1+=newBoltes
            numBottles=numBottles%numExchange
            numBottles=newBoltes+numBottles
        return sum1
