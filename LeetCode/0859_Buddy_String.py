class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        char_count = {}
        indexes_to_swap = []
        dup = False
        for idx, string in enumerate(A):
            curr_char_count = char_count.get(string, 0)
            curr_char_count += 1
            char_count[string] = curr_char_count
            if (curr_char_count > 1):
                dup = True
            if string != B[idx]:
                indexes_to_swap.append(idx)
                if len(indexes_to_swap) > 2:
                    return False
        
        if len(indexes_to_swap) == 1:
            return False
        
        if len(indexes_to_swap) == 2:
            return A[indexes_to_swap[0]] == B[indexes_to_swap[1]] and A[indexes_to_swap[1]] == B[indexes_to_swap[0]]
        return dup
