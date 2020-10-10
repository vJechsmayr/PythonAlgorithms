class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        string, pattern = [], []
        string[:0], pattern[:0] = s, p
        string.insert(0, 0) 
        pattern.insert(0, 0)
        s, p = len(string), len(pattern)
        dp = [[False for _ in range(p)] for __ in range(s)]
        dp[0][0] = True
        for i in range(p):
            if pattern[i] is '*' and dp[0][i-2]: dp[0][i] = True 
        for i in range(1, s):
            for j in range(1, p):
                if pattern[j] is string[i] or pattern[j] is '.':
                    dp[i][j] = dp[i-1][j-1]
                elif pattern[j] is '*' and (pattern[j-1] is string[i] or pattern[j-1] is '.'):
                    dp[i][j] = dp[i][j-2] or dp[i-1][j]
                elif pattern[j] is '*' and not (pattern[j-1] is string[i] or pattern[j-1] is '.'):
                    dp[i][j] = dp[i][j-2]
        return dp[s-1][p-1]
