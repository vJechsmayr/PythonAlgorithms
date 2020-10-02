class Solution:
    def canWinNim(self, n: int) -> bool:
         return (n & 0b11) != 0


print(Solution().canWinNim(7))