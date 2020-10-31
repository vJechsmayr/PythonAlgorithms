class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m = len(rowSum)
        n = len(colSum)
        matrix = [[0]*n for i in range(m)]
        print(matrix)
        for i in range(m):
            for j in range(n):
                matrix[i][j] = min(rowSum[i],colSum[j])
                rowSum[i] -= matrix[i][j]
                colSum[j] -= matrix[i][j]
        return matrix
        