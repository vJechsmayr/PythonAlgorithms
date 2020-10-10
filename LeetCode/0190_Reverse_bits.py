class Solution:
    def reverseBits(self, n: int) -> int:
        
        s='{0:032b}'.format(n)[::-1]
        return int(s,2)