class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
       #use some kind of binary sort logic here
        if len(matrix) > 0:
            i=0
            j=len(matrix[0])-1

            while ( i < len(matrix) and j >= 0 ):        
                if matrix[i][j] == target:
                    return True
                elif matrix[i][j] < target:
                    i += 1
                else:
                    j-=1