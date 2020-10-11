class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map_chars = {}
        longest = 0
        j = 0

        for i in range(0, len(s)):
            if s[i] in map_chars.keys():
                j = max(j, map_chars[s[i]] + 1)

            longest = max(longest, i - j + 1)
            map_chars[s[i]] = i

        return longest