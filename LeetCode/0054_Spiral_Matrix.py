class Solution:
    def spiralOrder(self, matrix):
        if len(matrix)>0:
            k, l = 0, 0
            m = len(matrix)
            n = len(matrix[0])

            l1 = []
            while (k < m and l < n):

                for i in range(l, n):
                    l1.append(matrix[k][i])

                k += 1

                for i in range(k, m):
                    l1.append(matrix[i][n - 1])
                n -= 1

                if (k < m):

                    for i in range(n - 1, (l - 1), -1):
                        l1.append(matrix[m - 1][i])

                    m -= 1

                if (l < n):
                    for i in range(m - 1, k - 1, -1):
                        l1.append(matrix[i][l])

                    l += 1
            return l1


        