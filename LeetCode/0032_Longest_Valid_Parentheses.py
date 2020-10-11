from typing import List, Dict

class Solution:
    def _score(self, position: List[int], state: Dict[int,bool]) -> List[int]:
        score = 0
        scores = list()
        for pos in position:
            matched = state.get(pos)
            if not matched:
                scores.append(score)
                score = 0

            else:
                score = score + 2

        scores.append(score)

        return scores

    def longestValidParentheses(self, s: str) -> int:
        scores = [0]
        state = dict()
        position = list()
        opened = list()
        closed = list()
        for p, paren in enumerate(s):
            if paren == "(":
                opened.append(p)
                position.append(p)
                state[p] = False

            elif paren == ")" and len(opened) > 0:
                op = opened.pop()
                state[op] = True

            else:
                scores.extend(self._score(position, state))
                state = dict()
                position = list()
                opened = list()
                closed = list()

        scores.extend(self._score(position, state))
        return max(scores)
