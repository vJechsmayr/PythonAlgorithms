class Solution:
    def bitwiseComplement(self, N: int) -> int:
        binary = bin(N)[2:]
        ans = ['0'] * len(binary)
        for i in range(len(binary)):
            if binary[i] == '0':
                ans[i] = '1'
            else:
                ans[i] = '0'
        return int(''.join(ans), 2)

