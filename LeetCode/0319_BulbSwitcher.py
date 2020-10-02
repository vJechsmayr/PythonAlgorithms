# The bulbs that will be turned on in the end will be the ones that are perfect squares.
# So we just have to find the perfect square less than n; Square root of which will be the answer.
# Contributed by: Sahil Bairagi

class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(n**(0.5))
