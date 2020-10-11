import itertools
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keyboard = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz",
        }

        pressed = [keyboard[c] for c in digits]

        return [''.join(p) for p in itertools.product(*pressed) if p != ()]