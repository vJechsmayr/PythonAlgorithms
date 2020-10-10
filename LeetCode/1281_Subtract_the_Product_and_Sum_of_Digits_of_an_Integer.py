class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        a = 1
        b = 0;
        while(n):
            a*=n%10
            b+=n%10
            n//=10
        return a - b
        
