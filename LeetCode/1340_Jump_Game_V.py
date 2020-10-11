class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        dp = [1] * len(arr)

        for i, _ in sorted(enumerate(arr), key=lambda x: x[1]):
            max_h = 0
            for j in range(i - 1, max(i - d - 1, -1), -1):
                max_h = max(max_h, arr[j])
                if max_h < arr[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
                else:
                    break

            max_h = 0
            for j in range(i + 1, min(i + d + 1, len(arr))):
                max_h = max(max_h, arr[j])
                if max_h < arr[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
                else:
                    break

        return max(dp)
