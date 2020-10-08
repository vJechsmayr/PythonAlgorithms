class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try:
            res = haystack.index(needle)
            return res
        except:
            return -1 if needle else 0
