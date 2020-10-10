class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        total_a = sum(A)
        total_b = sum(B)
        set_b = set(B)
        for candy in A:
            swap_item = candy + (total_b - total_a) / 2
            if swap_item in set_b:
                return [candy, candy + (total_b - total_a) / 2]