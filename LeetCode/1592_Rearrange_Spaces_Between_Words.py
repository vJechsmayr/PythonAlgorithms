class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = text.split()
        space_cnt = text.count(' ')
        
        if len(words) == 1:
            return words[0] + ' ' * space_cnt
        else:
            return (' '* (space_cnt // (len(words)-1))).join(words)+ ' ' * (space_cnt % (len(words)-1))