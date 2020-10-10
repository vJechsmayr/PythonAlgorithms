class Solution(object):
    def isGoodArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def gcd(a, b):
            if a == 0:
                return b
            if a > b:
                return gcd(b, a)
            return gcd(b % a, a)

        return reduce(gcd, nums) == 1
        
