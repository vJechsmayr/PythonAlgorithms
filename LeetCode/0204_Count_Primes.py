class Solution:
    def countPrimes(self, n: int) -> int:
        if (n==0 or n==1 or n==2):
            return(0)
        count=0
        for num in range(2,n):
            if num > 1:
                # check for factors
                for i in range(2,num):
                    if (num % i) == 0:
                        #not a prime
                        break 
                else:
                    #prime number
                    count=count+1
        return (count)
    