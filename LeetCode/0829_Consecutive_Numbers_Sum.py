class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        count = 1
        L = 1
        while( L * (L + 1) < 2 * N): 
            a = (1.0 * N - (L * (L + 1) ) / 2) / (L + 1) 
            if (a ==int(a) ): 
                count += 1
            L += 1
        return count
        