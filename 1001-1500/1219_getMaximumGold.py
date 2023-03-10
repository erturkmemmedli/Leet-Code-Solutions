class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        self.result = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col]:
                    value = grid[row][col]
                    visited = set()
                    self.dfs(grid, m, n, row, col, value, visited)
        return self.result
                
    def dfs(self, grid, m, n, row, col, value, visited):
        if (row,col) not in visited:
            visited.add((row,col))
            self.result = max(self.result, value)
            for r, c in (row-1,col),(row+1,col),(row,col-1),(row,col+1):
                if 0 <= r < m and 0 <= c < n and grid[r][c] and (r,c) not in visited:
                    self.dfs(grid, m, n, r, c, value + grid[r][c], visited)
            visited.discard((row,col))
        return
