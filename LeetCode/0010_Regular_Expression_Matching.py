class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m,n = len(s),len(p)
        
        DP = [[False for j in range(n+1)] for i in range(m+1)]  
        
        DP[0][0] = True
        
        for i in range(m+1):
            for j in range(1,n+1):
                if p[j-1]=="*":
                    DP[i][j] = DP[i][j-2] or i>0 and DP[i-1][j] and (s[i-1]==p[j-2] or p[j-2]==".")
                else:
                    DP[i][j] = i>0 and DP[i-1][j-1] and (s[i-1]==p[j-1] or p[j-1]==".")
        
        return DP[-1][-1]
