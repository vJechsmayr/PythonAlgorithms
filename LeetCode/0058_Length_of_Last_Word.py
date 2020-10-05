
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s[::-1]
        count = 0
        for i in s:
            if count == 0 and i == ' ':
                continue
            if i == ' ':
                break
            count +=1
        return count