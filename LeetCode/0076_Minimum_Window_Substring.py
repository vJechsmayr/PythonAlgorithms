from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        char_frequency = defaultdict(lambda: 0)
        for c in t:
            char_frequency[c] += 1
        chars_matched = 0

        start = 0
        res = ""

        for end in range(len(s)):
            right_char = s[end]
            if right_char in t:
                char_frequency[right_char] -= 1
                if char_frequency[right_char] == 0:
                    chars_matched += 1

            while start <= end and chars_matched == len(char_frequency):
                if res == "" or end-start+1 < len(res):
                    res = s[start:end+1]

                left_char = s[start]
                if left_char in t:
                    if char_frequency[left_char] == 0:
                        chars_matched -= 1
                    char_frequency[left_char] += 1
                start += 1

        return res
