class Solution:
    def grayCode(self, n: int) -> List[int]:

        x = [0]
        for i in range(n):
           
            x = x + [j+2**i for j in x][::-1]
        return x