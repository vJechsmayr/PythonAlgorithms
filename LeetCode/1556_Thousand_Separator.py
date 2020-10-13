class Solution:
    def thousandSeparator(self, n: int) -> str:
        num = n
        ans = f'{num:,}'.replace(',', '.')
        return ans


if __name__ == '__main__':
    x = Solution()
    answer = x.thousandSeparator(1234)
    print(answer)
