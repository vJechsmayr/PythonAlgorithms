class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        full = numBottles
        empty = 0
        drank = 0

        while True:
            # 1. Drink
            empty += full
            drank += full
            full = 0

            # 2. Exchange
            while empty >= numExchange:
                empty -= numExchange
                full += 1

            if not full:
                break

        return drank
