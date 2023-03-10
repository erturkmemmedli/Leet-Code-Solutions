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
