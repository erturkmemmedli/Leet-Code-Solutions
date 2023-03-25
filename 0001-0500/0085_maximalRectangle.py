class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        heights = [0] * (n + 1)
        maxArea = 0
        for i in range(m):
            for j in range(n):
                heights[j] = heights[j] + 1 if matrix[i][j] == '1' else 0
            stack = [-1]
            for k in range(n + 1):
                while stack and heights[k] < heights[stack[-1]]:
                    height = heights[stack.pop()]
                    width = k - 1 - stack[-1]
                    maxArea = max(maxArea, height * width)
                stack.append(k)
        return maxArea

# Alternative solution

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        heights = [0] * n
        max_area = 0

        for i in range(m):
            for j in range(n):
                heights[j] = int(matrix[i][j]) * heights[j] + int(matrix[i][j])
            
            max_area = max(max_area, self.largestRectangleArea(heights))

        return max_area

    def largestRectangleArea(self, heights):
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
