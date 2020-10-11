class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix)):
            for j in range(i,len(matrix)):
                if i != j:
                    matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for each in matrix:
            each.reverse()
        return matrix