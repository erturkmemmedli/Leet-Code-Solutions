from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        max_area = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if not grid[i][j] or (i, j) in visited:
                    continue
                Q = deque([(i, j)])
                area = 0
                while Q:
                    row, col = Q.popleft()
                    if (row, col) not in visited:
                        visited.add((row, col))
                        area += 1
                        for r, c in (row-1, col), (row+1, col), (row, col-1), (row, col+1):
                            if r >= 0 and c >= 0 and r < m and c < n and grid[r][c]:
                                Q.append((r, c))
                max_area = max(area, max_area)
        return max_area
