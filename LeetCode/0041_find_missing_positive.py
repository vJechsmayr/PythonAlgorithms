class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        hasOne = False;
        for i in range(len(nums)):
            if(nums[i]==1):
                hasOne = True
            if(nums[i]<0):
                nums[i] = 0
        
        if not hasOne:
            return 1
        
        for i in range(len(nums)):
            if(abs(nums[i])>0 and abs(nums[i])<=len(nums)):
                if(nums[abs(nums[i])-1]==0):
                    nums[abs(nums[i])-1]=-1
                elif(nums[abs(nums[i])-1]>0):
                    nums[abs(nums[i])-1]*=-1
                    
        for i in range(len(nums)):
            if nums[i]>=0:
                return i+1
        
        return len(nums)+1
