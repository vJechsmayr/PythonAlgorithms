class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        fin=[]
        for i in range(2**len(nums)):
            lst=[]
            for j in range(len(nums)):
                if i%2==1: lst.append(nums[j])
                i=i//2
                if i==0: break
            
            fin.append(sorted(lst))
            
        lst2=[]
        for x in fin:
            if not x in lst2:
                lst2.append(x)
            
        return sorted(lst2,key= lambda x: x[0] if x else -1 )