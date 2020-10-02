class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        digits.sort(reverse=True)
        N = len(digits)
        dp = [[float('-inf')] * N for _ in range(3)]
        for n in range(N):
            for k in [0, 1, 2, 0]:
                if n == 0 or (dp[k][n-1] == float('-inf') and dp[(k - digits[n]) % 3][n-1] == float('-inf')):
                    if digits[n] % 3 == k:
                        dp[k][n] = digits[n]
                else:
                    if digits[n] % 3 == 0:
                        dp[k][n] = dp[k][n-1] * 10 + digits[n]
                    else:
                        dp[k][n] = max(dp[k][n-1], dp[(k - digits[n]) % 3][n-1] * 10 + digits[n])

        return str(dp[0][-1]) if dp[0][-1] != float('-inf') else ''
