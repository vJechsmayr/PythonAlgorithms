class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        columns=len(grid[0])
        for i in range(1,columns):
            grid[0][i]+=grid[0][i-1]
        for j in range(1,rows):
            grid[j][0]+=grid[j-1][0]
        for k in range(1,rows):
            for l in range(1,columns):
                grid[k][l]+=min(grid[k][l-1],grid[k-1][l])
        return grid[-1][-1] 
