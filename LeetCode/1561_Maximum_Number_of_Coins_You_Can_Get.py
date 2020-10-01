class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        piles = piles[::-1]
        ans = 0
        n = len(piles) // 3
        for i in range(1, 2 * n, 2):
            ans += piles[i]
        return ans
