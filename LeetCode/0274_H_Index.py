class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        if n==0:
            return 0
        if set(citations) == {0}:
            return 0
        for i in range(n):
            if n-i<=citations[i]:
                return n-i