class Solution:
    def numSquares(self,n):
        dpa=[0]*(n+1)
        for x in range(1,n+1):
            min_value=x
            y,square=1,1
            while square<=x:
                min_value=min(min_value,1+dpa[x-square])
                y+=1
                square=y*y
                dpa[x]=min_value
        return dpa[n]

		
        



		
