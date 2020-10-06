class Solution:
    def reorderSpaces(self, text: str) -> str:
        
        if ' ' not in text:
            return text
        
        words, new_word, space_cnt = [], '', 0
        for l in text:
            if l == ' ':
                if new_word != '':
                    words.append(new_word)
                space_cnt += 1
                new_word = ''
            else:
                new_word = ''.join([new_word, l])
        if text[-1] != ' ':
            words.append(new_word)
        
        if len(words) > 1:
            return (' '* (space_cnt // (len(words)-1))).join(words)+ ' ' * (space_cnt % (len(words)-1))
        else:
            return words[0] + ' '* space_cnt