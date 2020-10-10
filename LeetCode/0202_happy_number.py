import numpy as np

def sum_of_squares(a):
    a = [int(d) for d in str(a)]
    a = list(np.array(a)**2)
    return sum(a)

class Solution(object):
    def isHappy(self, n):
        arr = []
        while True:
            n = sum_of_squares(n)
            if n in arr:
                return False
                
            else:
                if n==1:
                    return True
                    
                else:
                    arr.append(n)


        

