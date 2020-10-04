class Solution:
    def lengthOfLongestSubstring(self, s):
        li = [-1] * 256 #NUMBER OF CHARACTERS...
        n = len(s)
        res = 0
        i = 0

        for j in range(0, n):
            i = max(i, li[ord(s[j])] + 1) 
            res =  max(res, j - i + 1)
            li[ord(s[j])] = j;

        return res
    
