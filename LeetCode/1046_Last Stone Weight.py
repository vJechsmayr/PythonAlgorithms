import bisect
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        
        l=len(stones)
        while l>1:
        
            if stones[l-1]==stones[l-2]:
                stones.pop()
                stones.pop()
                l=l-2
            else:
                x=stones[l-1]-stones[l-2]
                
                stones.pop()
                stones.pop()
                bisect.insort(stones,x)
                l-=1
        try:
            return stones[0]
        except:
            return 0
                
            
        