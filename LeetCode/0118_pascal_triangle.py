class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==0:
            return []
        triangle=[[1]]
        for row in range(numRows-1):
            triangle.append([1]+[triangle[-1][i]+triangle[-1][i+1] for i in range(row)]+[1])
        return triangle
        