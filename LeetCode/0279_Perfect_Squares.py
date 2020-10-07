class Solution(object):
    def numSquares(self,n):
        if(n == 0):
            return 0
        if(n == 1):
            return 1
        squares = self.findSquares(n)
        rows = len(squares)
        cols = n + 1
        mat = [n] * cols
        mat[0] = 0

        for s in squares:
            for j in range(s,cols):
                mat[j] = min(mat[j], 1 + mat[j - s])

        return mat[n]

    def min(self,a,b):
        if(a <= b):
            return a
        else:
            return b

    def findSquares(self,n):
        i = 1
        squares = []
        while (i * i <= n):
            squares.append(i * i)
            i = i + 1
        return squares

x = Solution()
number = int(input())
print(x.numSquares(number))
