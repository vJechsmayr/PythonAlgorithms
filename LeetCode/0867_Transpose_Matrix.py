"""
Problem: Given a matrix A, return the transpose of A. The transpose of a matrix is the matrix flipped over it's main diagonal, switching the row and column indices of the matrix.

Sample input:
    [[1,2,3],
     [4,5,6],
     [7,8,9]]

Sample output:
    [[1,4,7],
     [2,5,8],
     [3,6,9]]
"""

class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        transpose=[]
        k=0
        for p in range(len(A[0])):
            temp=[]
            for i in A:
                while k<len(i):
                    temp.append(i[k])
                    break
            transpose.append(temp)
            k+=1
        return transpose
