class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        min_n = {min(rows) for rows in matrix}
        max_n = {max(columns) for columns in zip(*matrix)} 
        
        return list(min_n & max_n)
    
        