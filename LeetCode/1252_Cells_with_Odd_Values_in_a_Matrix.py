import numpy as np

class Solution:

    def get_summation_matrix(self, n: int, m: int, ri: int, ci: int):
        mat = np.zeros([n, m], dtype=int)
        mat[ri,:] += 1
        mat[:,ci] += 1
        return mat

    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        matrix_inc = sum(self.get_summation_matrix(n, m, ri, ci) for ri, ci in indices)
        return np.count_nonzero(matrix_inc % 2 == 1)
