from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs):

        stringsDict = defaultdict(list)
        for str in strs:
            stringsDict["".join(sorted(str))].append(str)
        ans = []
        for group in stringsDict.values():
            ans.append(group)

        return ans
