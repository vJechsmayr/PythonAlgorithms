class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        b = list(bin(n)[2:])
        temp = len(b)
        for i in range(1, temp):
            b[i] = str(int(b[i]) ^ int(b[i-1]))
        return int(''.join(b), 2)
