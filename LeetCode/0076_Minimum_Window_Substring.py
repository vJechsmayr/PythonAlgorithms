from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        char_frequency = defaultdict(lambda: 0)
        for c in pattern:
            char_frequency[c] += 1
        chars_matched = 0

        start = 0
        res = ""

        for end in range(len(string)):
            right_char = string[end]
            if right_char in pattern:
                char_frequency[right_char] -= 1
                if char_frequency[right_char] == 0:
                    chars_matched += 1

            while start <= end and chars_matched == len(char_frequency):
                if res == "" or end-start+1 < len(res):
                    res = string[start:end+1]

                left_char = string[start]
                if left_char in pattern:
                    if char_frequency[left_char] == 0:
                        chars_matched -= 1
                    char_frequency[left_char] += 1
                start += 1

        return res
