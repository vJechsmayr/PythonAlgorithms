class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_dict = dict()
        temp = []
        for i in range(len(s)):
            if s[i] not in temp:
                temp.append(s[i])
            else:
                temp_str = ''.join(temp)
                # temp.clear()
                temp = temp[temp.index(s[i])+1:]
                temp.append(s[i])
                my_dict[temp_str] = len(temp_str)
        temp_str = ''.join(temp)
        my_dict[temp_str] = len(temp_str)
        return max(my_dict.values())
