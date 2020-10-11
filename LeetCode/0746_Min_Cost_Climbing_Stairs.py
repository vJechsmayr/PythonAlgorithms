class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        l=len(cost)
        
        if l<=2:
            return 0
        a=[0]*l
        a[0]=cost[0]
        a[1]=cost[1]
        for i in range(2,l):
            a[i]=min(a[i-1],a[i-2])+cost[i]
        return min(a[l-1],a[l-2])
        
        
            
        