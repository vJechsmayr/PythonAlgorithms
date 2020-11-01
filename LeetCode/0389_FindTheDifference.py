class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        a = 0
        b = 0
        if 0 <= len(s) <= 1000:
            for chars in s:
                if 97 <= ord(chars) <= 122:
                    a += ord(chars)
            for letters in t:
                if 97 <= ord(letters) <= 122:
                    b += ord(letters)
            return chr(b - a)
