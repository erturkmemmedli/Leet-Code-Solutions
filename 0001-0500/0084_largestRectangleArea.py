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

# Alternative solution

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        i = 0

        while i < len(heights):
            max_area = max(max_area, heights[i])
            width = 1

            while stack and stack[-1][0] >= heights[i]:
                h, w = stack.pop()
                if stack and stack[-1][0] >= heights[i]:
                    stack[-1] = [min(stack[-1][0], h), stack[-1][1] + w]
                    max_area = max(max_area, stack[-1][0] * stack[-1][1])
                else:
                    width += w
                    max_area = max(max_area, min(h, heights[i]) * width)
                    break
        
            stack.append([heights[i], width])
            i += 1

        while len(stack) > 1:
            h, w = stack.pop()
            stack[-1] = [stack[-1][0], stack[-1][1] + w]
            max_area = max(max_area, stack[-1][0] * stack[-1][1])
            
        return max_area

# Alternative solution

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [[-float('inf'), 0]]
        max_area = 0

        for height in heights:
            width = 0
            h = stack[-1][0]

            while stack[-1][0] > height:
                h, w = stack.pop()
                width += w
                max_area = max(max_area, h * width)

            max_area = max(max_area, height * (width + 1))
            stack.append([height, width + 1])
        
        width = 0

        while len(stack) > 1:
            h, w = stack.pop()
            width += w
            max_area = max(max_area, h * width)
        
        return max_area
