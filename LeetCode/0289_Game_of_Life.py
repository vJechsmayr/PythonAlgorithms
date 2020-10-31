class Solution:
    def gameOfLife(self, board):
        self.m = len(board)
        self.n = len(board[0])
        self.board = [rows.copy() for rows in board]
        for i in range(self.m):
            for j in range(self.n):
                state = self.board[i][j]
                dataDict = self.CheckNeighbors(i,j)
                nextGen = self.NextGenState(state,dataDict)
                board[i][j] = nextGen


    def CheckNeighbors(self,row,column):
        retDict = {"live":0,"dead":0}
        lb = max(column-1,0)
        rb = min(column+2,self.n)
        tb = max(row -1,0)
        bb = min(row+2,self.m)
        for rows in range(tb,bb):
            for columns in range(lb,rb):
                if rows != row or columns != column :
                    neighbor = self.board[rows][columns]
                    if neighbor == 1:
                        retDict["live"] += 1
                    else:
                        retDict["dead"] += 1
        return retDict
            
    def NextGenState(self,state,dataDict):
        finalState = 0
        liveNeighbors = dataDict["live"]
        if state == 1:
            if liveNeighbors == 2 or liveNeighbors == 3:
                finalState = 1
        else:
            if liveNeighbors == 3:
                finalState = 1
        return finalState



