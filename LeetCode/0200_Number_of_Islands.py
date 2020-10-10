class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        cnt = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    cnt += 1
                    self.removeIsland(grid, i, j)
        return cnt

    # recursive function for replacing adjacent "1"s
    def removeIsland(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
            return
        if grid[i][j] == "0":
            return
        grid[i][j] = "0"
        self.removeIsland(grid, i+1, j)
        self.removeIsland(grid, i-1, j)
        self.removeIsland(grid, i, j+1)
        self.removeIsland(grid, i, j-1)
