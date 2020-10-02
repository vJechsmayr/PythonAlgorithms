class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        #   Pretty much same as combination sums II, use index at most once per combo
        
        #   create list from 1 to n
        #   for each i-th element, call helper function from [i+1:]
        #   from the helper function, if length of arr passed in == k
        #   append and return
        #   otherwise, keep going for i+1 in a for loop in the helper
        #   ^ after done, delete the last index(backtrack process)
        
        nums = [_ for _ in range(1,n+1)]
        result = []
        combo = []
        n = len(nums)
        
        for i in range(n):
            combo.append(nums[i])
            self.backtrack(nums[i+1:],combo, result, k)
            combo = []
            
        return result
    
    def backtrack(self, nums: List[int], combo: List[int], result: List[List[int]], k: int) -> None:
        
        if len(combo) == k:
            result.append([_ for _ in combo])
            return
        
        n = len(nums)
        
        for i in range(n):
            combo.append(nums[i])
            self.backtrack(nums[i+1:],combo,result,k)
            # This is the backtrack process
            del combo[-1]
            
        return