class Solution:
    def thousandSeparator(self, n: int) -> str:
        num = n
        ans = f'{num:,}'
        return ans


if __name__ == '__main__':
    x = Solution()
    answer = x.thousandSeparator(2**31)
    print(answer)
