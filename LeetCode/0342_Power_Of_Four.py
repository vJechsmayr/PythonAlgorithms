import math
class Solution:
    #Solution without loops/recursion
    def isPowerOfFour(self, num: int) -> bool:
        if(num!=0): #number 0 there isn't in the logarithmic function domain!
            exponent = math.log(abs(num), 4) #I will discover the number which multiply 4 nth times. The result must be equal to num. Ex: 4^2 = 16
            #However, the exponent must to be an integer value for num  to be a power of 4. For example, there are no 4's half number power!
            return int(math.pow(4, int(exponent)))==num
        return False #number zero was the input