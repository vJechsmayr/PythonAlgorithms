class Solution:
    def __init__(self):
        self.directionX = [-1,0,1,0]
        self.directionY = [0,1,0,-1]
    def isValid(self, x, y, N, M):
        if x < N and x >= 0 and y < M and y >= 0:
            return True
        return False
    
    def isCycle(self, x, y, arr, visited, parentX, parentY):
        # Mark the current vertex as visited
        visited[x][y] = True
        N, M = len(arr), len(arr[0])

        for k in range(4):
            newX = x + self.directionX[k]
            newY = y + self.directionY[k]
            if self.isValid(newX, newY, N, M) and arr[newX][newY] == arr[x][y] and not (parentX == newX and parentY == newY):
                if visited[newX][newY]:
                    return True
                else:

                    check = self.isCycle(newX, newY, arr, visited, x,y)
                    if check:
                        return True
        return False
    
    def containsCycle(self, grid: List[List[str]]) -> bool:
        N, M = len(grid), len(grid[0])
        # Initially all the cells are unvisited
        visited = [[False] * M for _ in range(N)]

        # Variable to store the result
        cycle = False

        # As there is no fixed position of the cycle
        # we have to loop through all the elements
        for i in range(N):
            if cycle == True:
                break

            for j in range(M):
                ## Taking (-1, -1) as source node's parent
                if visited[i][j] == False:
                    cycle = self.isCycle(i, j, grid, visited, -1, -1)

                if cycle == True:
                    break
        
        return cycle
        
        
        
        
        