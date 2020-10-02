class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        def scramble(s1, s2):
            key = (s1, s2)
            if key in mem:
                return mem[key]

            if sorted(s1) != sorted(s2):
                return False

            if s1 == s2:
                mem[key] = True
                return True

            for i in range(len(s1) - 1, 0, -1):
                if (scramble(s1[:i], s2[:i]) and scramble(s1[i:], s2[i:])) or (
                    scramble(s1[:i], s2[-i:]) and scramble(s1[i:], s2[:-i])
                ):
                    return True
            mem[key] = False
            return False

        mem = {}
        return scramble(s1, s2)
