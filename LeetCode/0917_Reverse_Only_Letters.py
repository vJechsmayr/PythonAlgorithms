class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        letters = []
        for c in S:
            if c.isalpha():
                letters.append(c)
        result = []
        for c in S:
            if c.isalpha():
                result.append(letters.pop())
            else:
                result.append(c)
        return ''.join(result)