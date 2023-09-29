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

# Alternative solution

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pacific = deque()
        atlantic = deque()

        for i in range(m):
            pacific.append((i, 0))
            atlantic.append((i, n - 1))

        for j in range(n):
            pacific.append((0, j))
            atlantic.append((m - 1, j))

        pacific_set = self.bfs(heights, pacific, m, n)
        atlantic_set = self.bfs(heights, atlantic, m, n)

        return pacific_set.intersection(atlantic_set)
        
    def bfs(self, grid, queue, m, n):
        dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited = set()

        while queue:
            r, c = queue.popleft()
            visited.add((r, c))

            for i, j in dir:
                row, col = r + i, c + j
                
                if m > row >= 0 <= col < n and (row, col) not in visited and grid[row][col] >= grid[r][c]:
                    visited.add((row, col))
                    queue.append((row, col))

        return visited
