class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dic = {}
        for word in wordDict:
            if len(word) in dic:
                dic[len(word)].append(word)
            else:
                dic[len(word)] = [word]
        dp = [True] + [False] * len(s)
        for i in range(len(s)):
            for k in dic:
                if i - k + 1 >= 0 and dp[i - k + 1] and s[i - k + 1 : i + 1] in dic[k]:
                    dp[i + 1] = True
        return dp[-1]
