class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
            t=tomatoSlices
            c=cheeseSlices
            return [int(t / 2 - c), int(c * 2 - t / 2)] if t % 2 == 0 and c * 2 <= t <= c * 4 else []
