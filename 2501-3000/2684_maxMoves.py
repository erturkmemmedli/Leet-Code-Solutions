class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        memo = {}
        res = 0

        def dp(row, col):
            if col == n - 1:
                return 1

            if (row, col) in memo:
                return memo[(row, col)]
            
            res = 1

            for i in [-1, 0, 1]:
                if 0 <= row + i < m and grid[row + i][col + 1] > grid[row][col]:
                    res = max(res, 1 + dp(row + i, col + 1))
                
            memo[(row, col)] = res
            return res

        for i in range(m):
            res = max(res, dp(i, 0) - 1)

        return res
