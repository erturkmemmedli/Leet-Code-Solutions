class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        toPacific = set()
        toAtlantic = set()
        m = len(heights)
        n = len(heights[0])
        for i in range(n):
            self.dfs(heights, m, n, 0, i, toPacific)
            self.dfs(heights, m, n, m-1, i, toAtlantic)
        for i in range(m):
            self.dfs(heights, m, n, i, 0, toPacific)
            self.dfs(heights, m, n, i, n-1, toAtlantic)
        return toPacific - (toPacific - toAtlantic)

    def dfs(self, heights, m, n, row, col, visited):
        if (row, col) in visited:
            return
        visited.add((row, col))
        for r, c in (row + 1, col), (row, col + 1), (row - 1, col), (row, col - 1):
            if 0 <= r < m and 0 <= c < n and heights[r][c] >= heights[row][col] and (r, c) not in visited:
                self.dfs(heights, m, n, r, c, visited)
