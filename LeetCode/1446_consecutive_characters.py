class Solution:
    def maxPower(self, s: str) -> int:
        maxlen,currlen=1,1
        for i in range(1,len(s)):
            if(s[i]==s[i-1]):
                currlen=currlen+1
                maxlen=max(maxlen,currlen)
            else:
                currlen=1
        return maxlen