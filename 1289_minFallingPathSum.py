class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 1: return grid[0][0]
        for i in range(1, n):
            small, big, index = float('inf'), float('inf'), None
            for k in range(n):
                if grid[i-1][k] <= small:
                    small, big, index = grid[i-1][k], small, k
                elif grid[i-1][k] < big:
                    big = grid[i-1][k]
            for j in range(n):
                if j == index:
                    grid[i][j] += big
                else:
                    grid[i][j] += small
        return min(grid[-1])
