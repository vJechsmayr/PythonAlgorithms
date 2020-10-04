class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        self.k = k
    
        def backtrack(path, remain):
            if not remain:
                self.k -= 1
                if self.k == 0:
                    return path
                return ''
                
            for i in range(len(remain)):
                if self.k > math.factorial(len(remain)-1):
                    self.k -= math.factorial(len(remain)-1)
                    continue
                ans = backtrack(path + remain[i], remain[:i]+remain[i+1:])
                if ans: 
                    return ans
            return ''
        nums = list(map(str, range(1, n+1)))
        return backtrack('', nums)
