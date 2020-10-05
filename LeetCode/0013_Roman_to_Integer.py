class Solution:
    def romanToInt(self, s: str) -> int:
        value = {'M': 1000,'D': 500, 'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
        p = 0;ans = 0
        n = len(s)
        for i in range(n-1, -1, -1):
            if value[s[i]] >= p: 
                ans += value[s[i]]
            else:
                ans -= value[s[i]] 
            p = value[s[i]]
        return ans
