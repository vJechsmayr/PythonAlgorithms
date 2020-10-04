def gray(a):
	return ((a)^(a>>1))

class Solution:
    def grayCode(self, n: int) -> List[int]:
        ans=[]
        for i in range(pow(2,n)):
        	ans.append(gray(i))
        return ans 

	
