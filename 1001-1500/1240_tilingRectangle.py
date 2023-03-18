class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        self.min_squares = m * n
        self.dfs([0] * m, 0, n, m)
        return self.min_squares

    def dfs(self, heights, moves, n, m):
        if moves >= self.min_squares:
            return
        
        if all(height == n for height in heights):
            self.min_squares = min(self.min_squares, moves)
            return

        i = j = heights.index(min(heights))

        while j < m and heights[i] == heights[j]:
            j += 1

        for k in range(min(j - i, n - heights[i]), 0, -1):
            self.dfs(heights[:i] + [heights[i] + k] * k + heights[i + k:], moves + 1, n, m)
