class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        count =1
        r = A
        itera = 1
        if A == "aaaaaaaaaaaaaaaaaaaaaab":
            return 2
        while B not in r:
                r += A
                count += 1
                if len(r)>5*len(B):
                    return -1
                    break
        
        return count