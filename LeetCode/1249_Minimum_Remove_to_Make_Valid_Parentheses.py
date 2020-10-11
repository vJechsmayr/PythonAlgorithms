class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        stackparen = []
        stackindex = []
        result = ''
        result1 = ''
        i = 0
        j = 0

        while i <= len(s) - 1:
            if s[i] == ')' and len(stackparen) == 0:
                i += 1
                continue
            if s[i] == '(':
                stackparen.append(s[i])
                stackindex.append(j)
            if s[i] == ')' and len(stackparen) > 0:
                stackparen.pop()
                stackindex.pop()
            result += s[i]
            j += 1
            i += 1

        for j, i in enumerate(result):
            if j not in stackindex:
                result1 += result[j]
        return result1
