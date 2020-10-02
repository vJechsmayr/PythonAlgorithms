class Solution:
    ans = 0
    def findPathNum(self, i, j, grid: List[List[int]], curLen, pLen)->None:
        if(grid[i][j]==2):
            if(pLen-1==curLen):
                self.ans+=1
            return
        elif (grid[i][j]==-1):
            return
        curLen+=1 
        grid[i][j]=-1
        if(i-1>=0):
            self.findPathNum(i-1, j, grid, curLen, pLen)
        if(j-1>=0):
            self.findPathNum(i, j-1, grid, curLen, pLen)
        if(i+1<len(grid)):
            self.findPathNum(i+1, j, grid, curLen, pLen)
        if(j+1<len(grid[0])):
            self.findPathNum(i, j+1, grid, curLen, pLen)
        grid[i][j]=0
        
            
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        pathLen = 0
        start = (0, 0)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j]!=-1):
                    pathLen+=1
                    if(grid[i][j]==1):
                        start = (i, j)
        self.findPathNum(start[0], start[1], grid, 0, pathLen)
        return self.ans
        
