class Solution(object):
  
    def lengthOfLastWord(self, s):
        length = 0
        for i in reversed(s):
            if i == ' ':
                if length:
                    break
            else:
                length += 1
        return length
class Solution2(object):
   
    def lengthOfLastWord(self, s):
        return len(s.strip().split(" ")[-1])
