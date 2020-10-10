class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
        i = 1
        sum_odds = 0
        while sum_odds < num: 
            sum_odds += i 
            if sum_odds == num: 
                return True
            i += 2
        return False