class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        
        ways = [[0 for j in range(m)] for i in range(n)]
        
        for i in range(n):
            if obstacleGrid[i][0] == 1:
                break
            ways[i][0] = 1
        
        for j in range(m):
            if obstacleGrid[0][j] == 1:
                break
            ways[0][j] = 1
        
        for i in range(1, n):
            for j in range(1, m):
                if obstacleGrid[i][j] == 0:
                    ways[i][j] = ways[i - 1][j] + ways[i][j - 1]
        
        return ways[n - 1][m - 1]
