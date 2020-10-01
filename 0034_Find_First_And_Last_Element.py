class Solution:
    
    def first_pos(self,a: List[int],x : int)-> int:
        n = len(a)
        pos = n
        low = 0 
        high = n-1
        while(low <= high ):
            mid = (low +high)//2
            if(a[mid] >= x):
                pos = mid
                high = mid-1
            else:
                low = mid+1
        return pos
        
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = self.first_pos(nums,target)
        last =  self.first_pos(nums,target+1)-1
        if (first<=last):
            return [first,last]
        else:
            return [-1,-1]
        
        
      