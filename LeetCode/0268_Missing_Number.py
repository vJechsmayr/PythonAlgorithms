class Solution:
    def computeXOR(self,n:int) -> int:
        if n%4==0:
            return n
        elif n%4==1:
            return 1
        elif n%4==2:
            return n+1
        else:
            return 0
    def missingNumber(self, nums: List[int]) -> int:
        all_xor = self.computeXOR(len(nums))
        current_xor = 0
        for i in nums:
            current_xor^=i
        return(all_xor^current_xor)