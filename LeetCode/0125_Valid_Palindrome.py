import re

class Solution:
    def isPalindrome(self, s: str):
        s=re.sub("[\W_]*","",s).lower()
        if s[::-1]==s:
            return True
        else:
            return False
