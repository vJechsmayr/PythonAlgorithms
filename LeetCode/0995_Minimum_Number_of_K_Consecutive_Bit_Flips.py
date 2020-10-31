class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        n = len(A)
        flips = [0]*(n+1); ans = 0
        for i in range(n):
            flips[i] += flips[i-1] if i > 0 else 0
            
            if not A[i] ^ (flips[i]%2):
                if i + K - 1 >= n :
                    print(i, K)
                    return -1
                ans += 1
                flips[i] += 1
                flips[i+K] -= 1
            
        return ans
            
                