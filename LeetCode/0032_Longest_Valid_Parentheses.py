class Solution:
    def longestValidParentheses(self, s: str) -> int:
        state = 0
        tokens = list()
        for paren in s:
            if paren == "(":
                state = state - 1
                tokens.append(-1)

            elif paren == ")" and state < 0:
                state = state + 1
                tokens.append(1)

            else:
                tokens.append(0)

        token_sets = [list()]
        for token in tokens:
            if token == 0:
                token_sets.append(list())
                continue

            token_sets[-1].append(token)

        valid_sets = [0]
        for token_set in token_sets:
            for offset in range(len(token_set)-1):
                for nudge in range(offset+1):
                    offset_front = offset - nudge
                    offset_back = len(token_set) - nudge
                    offset_tokens = token_set[:][offset_front:offset_back]

                    invalid = True
                    while invalid:
                        check = 0
                        front = offset_tokens[0]
                        if front in [1, 0]:
                            offset_tokens = offset_tokens[1:]
                            check = check + 1

                        back = offset_tokens[-1]
                        if back in [-1, 0]:
                            offset_tokens = offset_tokens[:-1]
                            check = check + 1

                        if check == 0:
                            invalid = False

                        if len(offset_tokens) < 2:
                            break

                    if not invalid and sum(offset_tokens) == 0:
                        valid_sets.append(len(offset_tokens))
                        continue

        return max(valid_sets)
