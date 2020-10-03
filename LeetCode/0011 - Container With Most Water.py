class Solution(object):
    def maxArea(self, height):
        i=0
        j=len(height)-1
        a=0
        b=0
        while i<j:
            if height[i]<height[j]:
                b=(j-i)*height[i]
                i+=1
            else:
                b=(j-i)*height[j]
                j-=1
            if b>a:
                a=b
        return a