class Solution:
    def countSubstrings(self, s: str) -> int:
        N = len(s)
        # declaring a DP matrix of size nxn
        dp = [[0 for i in range(N)] for j in range(N)]
        # looping through substring of every size and checking whether it is a valid substring
        for l in range(N):
            for i in range(N-l):
                if l == 0:
                    dp[i][i] = 1
                    continue
                if s[i] == s[i+l]:
                    if l == 1:
                        dp[i][i+l] = 1
                    elif dp[i+1][i+l-1] == 1:
                        dp[i][i+l] = 1
        count = 0
        for i in range(N):
            for j in range(N):
                count+=dp[i][j]
        return count