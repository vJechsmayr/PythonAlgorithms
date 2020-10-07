class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            res = ""

        elif len(strs) == 1:
            res = strs[0]

        else:
            strs.sort()
            res = ""

            for i in range(len(strs[0])):
                if strs[0][i] == strs[-1][i]:
                    res += strs[0][i]
                else:
                    break

        return res
