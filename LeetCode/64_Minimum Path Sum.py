class Solution:
    def minPathSum(self, array: List[List[int]]) -> int:
        def find(array,m,n):
            for i in range(1,m):
                for j in range(1,n):
                    array[i][j]=min(array[i][j]+array[i-1][j],array[i][j]+array[i][j-1])     #comapre two values if we come from top or if we come from left whichever is minimum take it  and add the current value to it
            return array[m-1][n-1]



        m=len(array)
        n=len(array[0])
        for i in range(1,m):
            array[i][0]=array[i-1][0]+array[i][0]  #find the cost of traversing the first row and first column since these value will not depend on past values
        for i in range(1,n):
            array[0][i]=array[0][i-1]+array[0][i]
        return (find(array,m,n))
