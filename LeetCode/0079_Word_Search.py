def exist(self, grid: List[List[str]], word: str) -> bool:
    
    seen = set()

    # Boundary checking
    def inBound(row, col, grid):
        return 0 <= row < len(grid) and 0 <= col < len(grid[0])

    def dfs(grid, word, curr_i, row, col):
        
        if curr_i == len(word):
            return True
        
        if not inBound(row, col,grid) or grid[row][col] != word[curr_i]:
            return False
        
        seen.add((row, col))

        # Explore possible paths
        pos_paths = [(row, col + 1), (row, col - 1), (row + 1, col), (row - 1, col)]
        for row_n, col_n in pos_paths:
            if (row_n,col_n) not in seen:
                if dfs(grid, word, curr_i + 1, row_n, col_n):
                    return True

        seen.remove((row,col))
        return False

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == word[0]:
                if dfs(grid, word, 0, row, col):
                    return True
            
    return False