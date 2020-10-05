class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        length = 0
        for char in s[::-1]:
            if char != ' ':
                length += 1
            elif char == ' ' and length > 0:
                return length
        return length