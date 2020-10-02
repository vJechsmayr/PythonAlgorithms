class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res, lo = [[n*n]], n*n
        while lo > 1:
            lo, hi = lo - len(res), lo
            #print('res:', res)
            res = [[i for i in range(lo, hi)]] + [list(j) for j in zip(*res[::-1])]
        return res
