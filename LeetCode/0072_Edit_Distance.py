class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
        m=len(word1)
        n=len(word2)
        dp=[[0 for i in range(n+1)] for j in range(m+1)]
        for i in range(m+1):
            dp[i][0]=i
        for j in range(n+1):
            dp[0][j]=j
        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=min(dp[i-1][j]+1,dp[i][j-1]+1,dp[i-1][j-1]+1)
        return dp[m][n]
 
test=Solution()
input1=str(input(“Enter a string1”))
input2=str(input(“Enter a string2”))
print(test.minDistance(input1,input2))
