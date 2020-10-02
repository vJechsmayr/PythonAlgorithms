import textwrap

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        substringLength:int = 0
        substrings:List = []
            
        while substringLength < len(s)/2:
            substringLength += 1
            if len(s)%substringLength != 0:
                continue

            substrings = textwrap.wrap(s, substringLength)
            if substrings[1:] == substrings[:-1] and len(substrings) > 1:
                return True
            
        return False
