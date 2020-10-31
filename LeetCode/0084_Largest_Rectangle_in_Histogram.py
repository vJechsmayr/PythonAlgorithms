class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        lst = [-1]
        output = 0

        for i in range(len(heights)):
            while (heights[i] < heights[lst[-1]]):
                height = heights[lst.pop()]
                width = i - lst[-1] - 1
                output = max(output, height * width)
            lst.append(i)

        heights.pop()
        return output
