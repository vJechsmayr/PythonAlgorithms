class Solution(object):
    cnt = 0
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.cnt = 0
        n = len(s)
        for i in range(n):
            self.palindromic(s, i, i) # judge odd length string
            self.palindromic(s, i, i+1) # judge even length string
        return self.cnt
        
    
    def palindromic(self, s, left, right): # judge if a substring is palindromic
        n = len(s)
        while(left >= 0 and right < n and s[left] == s[right]):
            self.cnt += 1
            left -= 1
            right += 1
