def finder(s):
        a =0
        for i in range(len(s) -1):
            if abs(ord(s[i]) - ord(s[i+1])) == 32 :
                del s[i]
                del s[i]
                a =1
                break
        if a == 0 :
            return s
        else:
            return finder(s)

class Solution:
    def makeGood(self, s: str) -> str:
        s = list(s)
        h = finder(s)
        return ("".join(h))