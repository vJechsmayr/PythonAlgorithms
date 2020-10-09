class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def isValid(s: str) -> bool:
            stk = []
            for b in s:
                if b == '(':
                    stk.append(b)
                else:
                    if stk and stk[-1] == '(':
                        stk.pop()
                    else:
                        return False
            return stk == []
        
        ans = []
        for mask in range(1<<(2*n)):
            s = ""
            for bit in range(2*n):
                if mask & (1<<bit):
                    s += '('
                else:
                    s += ')'
            if isValid(s):
                ans.append(s)
        return ans
