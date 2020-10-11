class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m=max(candies)
        t=m-extraCandies
        output=[]
        for i in candies:
            if i<t:
                output.append(False)
            else:
                output.append(True)
        return output