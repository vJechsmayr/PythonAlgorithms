class Solution:
    def thousandSeparator(self, n: int) -> str:
        num = n
        ans = f'{num:,}'.replace(',', '.')
        return ans
