class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        heights.append(0)
        stack = [-1]
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1
                maxArea = max(maxArea, height * width)
            stack.append(i)
        return maxArea
