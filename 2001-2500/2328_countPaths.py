class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        self.memo = {}
        return sum(self.dp(grid, m, n, i, j) for i in range(m) for j in range(n)) % 1_000_000_007

    def dp(self, grid, m, n, r, c):
        if (r, c) in self.memo:
            return self.memo[(r, c)]
        
        result = 1

        for row, col in [r-1, c], [r+1, c], [r, c-1], [r, c+1]:
            if m > row >= 0 <= col < n:
                if grid[row][col] > grid[r][c]:
                    result += self.dp(grid, m, n, row, col) % 1_000_000_007

        self.memo[(r, c)] = result
        return result
