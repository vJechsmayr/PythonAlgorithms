'''
Problem:-
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

The answer is guaranteed to fit in a 32-bit integer.

Example 1:

Input: s = "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).

Example 2:

Input: s = "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
'''

class Solution:
    def numDecodings(self, s: str) -> int:
        @lru_cache(None)
        def dp(i):
            if i == len(s):
                return 1
            ans = 0
            if s[i] != '0':
                ans += dp(i+1)
            if s[i] == '1' and i+1< len(s):
                ans += dp(i+2)
            if s[i] == '2' and i+1 < len(s) and s[i+1] <= '6':
                ans += dp(i+2)
            return ans        
        return dp(0)
