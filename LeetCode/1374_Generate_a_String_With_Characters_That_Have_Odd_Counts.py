class Solution:
    def generateTheString(self, n: int) -> str:
        ans=[]
        if n%2==0:
            ans=['x' for i in range(n-1)]
            ans.append('y')
        else:
            ans=['x' for i in range(n)]
        return ans
        