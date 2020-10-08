class Solution:
    def largestRectangleArea(self, ar: List[int]) -> int:
        n=len(ar)
		
		# next smaller right side
        def sr(ar,n):
            stack=[0]
            ans=[n] *n
            for i in range(1,n):
                while stack and ar[stack[-1]]>=ar[i]:
                    x=stack.pop()
                    ans[x]=i
                stack.append(i)
            return ans
			
       
		def sl( ar,n):
            stack=[n-1]
            ans=[-1] *n
            for i in range(n-2,-1,-1):
                while stack and ar[stack[-1]]>ar[i]:
                    x=stack.pop()
                    ans[x]=i
                stack.append(i)
            return ans
			
        la=sl(ar,n)
        ra=sr(ar,n)
        width=[]
		
        for i in range(n):
            width.append(ra[i]-la[i]-1)
        ans=0
		
        for i in range(n):
            ans=max(ans,width[i]*ar[i])
        return ans