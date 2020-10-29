class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 32 bits integer max and min
        MAX = 0x7FFFFFFF
        MIN = 0x80000000
        
        mask = 0xFFFFFFFF
        
        while b != 0:
            carry = a & b
            a, b = (a ^ b) & mask, (carry << 1) & mask
            
        return a if a <= MAX else ~(a ^ mask)