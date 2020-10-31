class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        indexes_to_swap = []
        for idx, string in enumerate(A):
            if string != B[idx]:
                indexes_to_swap.append(idx)
                if len(indexes_to_swap) > 2:
                    return False
        
        if len(indexes_to_swap) != 2:
            return false
        
        return A[indexes_to_swap[0]] == B[indexes_to_swap[1]] and A[indexes_to_swap[1]] == B[indexes_to_swap[0]]
