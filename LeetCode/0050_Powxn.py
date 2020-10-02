class Solution:
    def myPow(self,x: float, n: int) -> float:
        if n == -1:
            return 1/x
        elif n == 1:
            return x
        elif n == 0:
            return 1
        if n%2 == 0:
            return self.myPow(x*x,n//2)
        else:
            return self.myPow(x*x,n//2) * x
    
    

