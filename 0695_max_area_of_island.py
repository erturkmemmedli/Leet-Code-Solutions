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

# Alternative solution

class Solution1:
    def __init__(self):
        self.max_area = 0
        self.area = 0
        
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if not grid[i][j] or (i, j) in visited:
                    continue
                self.area = 0
                self.dfs(grid, i, j, m, n, self.max_area, self.area, visited)
        return self.max_area
                
    def dfs(self, grid, row, col, m, n, max_area, area, visited):
        if (row, col) not in visited:
            visited.add((row, col))
            self.area += 1
            self.max_area = max(self.max_area, self.area)
            for r, c in (row-1, col), (row+1, col), (row, col-1), (row, col+1):
                if r >= 0 and c >= 0 and r < m and c < n and grid[r][c]:
                    self.dfs(grid, r, c, m, n, self.max_area, self.area, visited)
        return          
