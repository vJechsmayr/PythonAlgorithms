class Solution:
    def isHappy(self, n):
        def squareSum(num):
            res = 0
            while num > 0:
                r = num%10
                res+=r*r
                num = num//10
            return res
        set1 = set()
        while squareSum(n) not in set1:
            temp_sum = squareSum(n)
            if temp_sum == 1:
                return True
            else:
                set1.add(temp_sum)
                n = temp_sum
        return False
        
