class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = [(n, n, [])]

        while stack:
            open_parens, close_parens, buffer = stack.pop()
            if open_parens == 0 and close_parens == 0:
                res.append("".join(buffer))

            if open_parens > 0:
                buffer.append("(")
                stack.append((open_parens - 1, close_parens, buffer.copy()))
                buffer.pop()

            if open_parens < close_parens:
                buffer.append(")")
                stack.append((open_parens, close_parens - 1, buffer.copy()))

        return res
