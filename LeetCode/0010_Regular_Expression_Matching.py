class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        count_len = 0
        previous_char,next_char = None, None
        for i in range(len(p)):
            if count_len <= len(s):
                if i < len(p)-1:
                    next_char = p[i+1]
                else:
                    next_char = None
                    
                if( (p[i] != '.') and (p[i] != '*') and next_char == '*'):
                        previous_char = p[i]
                        pass
                elif ( (p[i] != '.') and (p[i] != '*') ):
                    if p[i] != s[count_len]:
                        return False
                    count_len += 1
                            
                elif p[i]=='.':
                    count_len += 1
                else:
                    if previous_char == '.':
                        return True
                    while(count_len < len(s)):
                        if previous_char != s[count_len]:
                            break
                        else:
                            count_len += 1
                        
                previous_char = p[i]
                    
            else:
                break
        if count_len < len(s):
            return False
        else:
            return True
        
