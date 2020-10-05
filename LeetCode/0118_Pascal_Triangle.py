from typing import List

class Solution(object):
    def generate(
        self,
        num_rows: int,
        triangle: List[List[int]] = [[1]],
        last_row: int = 1
    ) -> List[List[int]] :
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if num_rows < last_row:  return []
        if num_rows == last_row: return triangle
        triangle.append([sum(i) for i in zip([*triangle[-1], 0], [0, *triangle[-1]])])
        return self.generate(num_rows, triangle, last_row+1)
