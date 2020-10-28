class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        mx = 0
        mn = 0
        res = [0] * (len(S) + 1)
        for i in range(len(S)):
            if S[i] == "I":
                res[i + 1] = mx + 1
                mx += 1
            else:
                res[i + 1] = mn - 1
                mn -= 1
        return [x - mn for x in res]
