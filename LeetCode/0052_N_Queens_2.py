class Solution(object):
    # @return an integer
    def totalNQueens(self, n):
        return self.totalNQueensRecu([], 0, n)

    def totalNQueensRecu(self, solution, row, n):
        if row == n:
            return 1
        result = 0
        for i in xrange(n):
            if i not in solution and reduce(lambda acc, j: abs(row - j) != abs(i - solution[j]) and acc, xrange(len(solution)), True):
                result += self.totalNQueensRecu(solution + [i], row + 1, n)
        return result