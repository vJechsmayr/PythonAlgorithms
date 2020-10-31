class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        stones = Counter(S)
        count = 0
        for j in J:
            if stones and j in stones:
                count += stones[j]
        return count
