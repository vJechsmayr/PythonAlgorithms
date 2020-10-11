class Solution(object):
    def find132pattern(self, nums: List[int]):
        if not nums or len(nums)< 2:
            return False

        m=0
        ln=len(nums)
        for i in range(len(nums)-1, -1, -1):
            n=nums[i]
            if i+1<ln and n>nums[i+1]:
                break
            else:
                m+=1
        else:
            return False

        ln-=m
        assert(ln and m)
        mi=ln
        s3mx=nums[ln-1]
        ln-=1

        s2mx=nums[mi]
        while mi<len(nums) and nums[mi]<s3mx:
            s2mx=nums[mi]
            mi+=1

        mx2=s2mx
        
        for i in range(ln-1, -1, -1):
            n=nums[i]
            if n<s2mx:
                return True
            elif n==s3mx and mx2>s2mx:
                s2mx=mx2
            elif n>s3mx:
                s2mx=s3mx
                s3mx=n
                while mi<len(nums) and nums[mi]<=s2mx:
                    mi+=1
                if mi<len(nums) and nums[mi]<s3mx:
                    s2mx=nums[mi]
                    mi+=1
            elif n>mx2 and n<s3mx:
                mx2=n

        return False