class Solution(object):
    def sumSubseqWidths(self, A: List[int]) -> int:
        ret_int = 0
        A_len = len(A)
        A.sort(key=lambda x: int(x), reverse=True)

        for x in range(A_len):
            ret_int += A[x] * (2**(A_len - x - 1) - 2**(x))

        return ret_int % (10**9 + 7)
