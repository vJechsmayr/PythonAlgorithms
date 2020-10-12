class Solution:
    def getSum(self, x: int, y: int) -> int:
        while (y != 0): 
      
            carry = x & y 
 
            x = x ^ y 
  
            y = carry << 1
      
        return x 
