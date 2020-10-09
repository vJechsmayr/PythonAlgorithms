class Solution(object):
    def isMatch(self, s, p):
        n = len(p)
        m = len(s)
        index = -1
        dp = [[False for i in range(n+5)] for j in range(m+5)]  
        dp[0][0] = not False
        for i in range(m+1):
            for j in range(1,n+1):
                if (p[j-1]!='*'):
                    dp[i][j] = i>0 and dp[i-1][j-1] and (s[i-1]==p[j-1] or p[j-1]=='.')
                else:
                    dp[i][j] = dp[i][j-2] or i>0 and dp[i-1][j] and (s[i-1]==p[j-2] or p[j-2]=='.')
        return dp[index][index]

        