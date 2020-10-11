---
name:  Longest Common Prefix
title: 0014_ Longest_Common_Prefix
labels: 'hacktoberfest'
assignees: 'grpnpraveen'

---

## Description of the Problem
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

## Code
```
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return '' 
        res = ''
        strs = sorted(strs)
        for i in strs[0]:
            if strs[-1].startswith(res+i):
                res += i
            else:
                break
        return res
```

## Link To The LeetCode Problem
[LeetCode](https://leetcode.com/problems/longest-common-prefix/)
