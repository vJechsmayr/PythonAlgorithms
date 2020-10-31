class Solution:
    def getMaximumGold(self, grid):
        def bfs(i, j):
            stack = [(grid[i][j], i, j, set([(i, j)]))]
            while stack:
                temp = []
                for cur, i, j, p in stack:
                    if cur > self.res:
                        self.res = cur
                        self.best_res = p
                    for x, y in [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]:
                        if 0 <= x < m and 0 <= y < n and grid[x][y] and (x, y) not in p:
                            temp.append((cur + grid[x][y], x, y, p | {(x, y)}))
                stack = temp
        m, n = len(grid), len(grid[0])
        self.res = 0
        self.best_res = set()
        for row in range(m):
            for col in range(n):
                if grid[row][col] and (row, col) not in self.best_res:
                    bfs(row, col)
        return self.res
