class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
            if a != b:
                 return max(len(a), len(b))
            else:
                return -1 