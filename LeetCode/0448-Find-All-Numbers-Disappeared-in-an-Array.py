class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        List=[]
        for i in range(len(nums)):
            val= abs(nums[i])-1
            if(nums[val]>0):
                nums[val]=-nums[val]
        for i in range(len(nums)):
            if(nums[i]>0):
                List.append(i+1)
        return List
        
