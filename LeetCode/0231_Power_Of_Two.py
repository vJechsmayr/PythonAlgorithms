class Solution:
    def isPowerOfTwo(self, x: int) -> bool:
        return (x != 0) and ((x & (x - 1)) == 0);