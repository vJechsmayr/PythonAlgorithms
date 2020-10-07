class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ans=0
        i=0
        curlen=len(nums)
        while i < curlen:
            if i==0 or i==1:
                ans+=1
            elif not (nums[i]==nums[i-1] and nums[i-1]==nums[i-2]):
                ans+=1
            elif nums[i]==nums[i-1] and nums[i-1]==nums[i-2]:
                j=i
                while j < curlen-1:
                    nums[j]=nums[j+1]
                    j+=1
                curlen-=1
                i-=1
            i+=1
        return ans