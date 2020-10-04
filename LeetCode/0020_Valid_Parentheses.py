class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openbrackets = ('(', '[', '{')
        matches = ('()', '[]', '{}')

        for c in s:
            if c in openbrackets:
                stack.append(c)
            else:
                if len(stack) < 1 or stack[-1] + c not in matches:
                    return False

                stack.pop()

        return len(stack) == 0