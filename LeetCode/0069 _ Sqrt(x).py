class Solution(object):
    def mySqrt(self, x):
        if x<2:
            return x
        low = 0
        high = x
        result=0
        while(low<=high):
            mid = (low+high)//2
            if(mid*mid==x):
                return mid
            elif(mid*mid<x):
                low = mid+1
                result = mid
            else:
                high = mid-1
        return result