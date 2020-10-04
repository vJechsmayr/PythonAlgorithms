class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = (1 << 31) - 1
        INT_MIN = -(1 << 31)

        ret = 0
        s = s.strip()

        if s == "":
            return ret

        negate = -1 if s[0] == '-' else 1

        if s[0] in ('+', '-'):
            s = s[1::]

        for c in s:
            if not '0' <= c <= '9':
                break

            ret = ret * 10 + ord(c) - ord('0')

        ret *= negate
        ret = min(max(ret, INT_MIN), INT_MAX)

        return ret