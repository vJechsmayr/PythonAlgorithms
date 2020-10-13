class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        maxGroupSize= max(groupSizes)
        groups = [[] for i in range(maxGroupSize)]
        
        for i, p in enumerate(groupSizes):
            groups[p-1].append(i)
            if len(groups[p-1]) == p:
                groups.append(groups[p-1])
                groups[p-1] = []

        return groups[maxGroupSize:]
