class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        memo = {}

        def dp(row, col):
            if row == m:
                return col

            if (row, col) in memo:
                return memo[(row, col)]

            if grid[row][col] == 1:
                if col + 1 < n and grid[row][col + 1] == 1:
                    memo[(row, col)] = dp(row + 1, col + 1)
                else:
                    memo[(row, col)] = -1

            if grid[row][col] == -1:
                if col - 1 >= 0 and grid[row][col - 1] == -1:
                    memo[(row, col)] = dp(row + 1, col - 1)
                else:
                    memo[(row, col)] = -1
            
            return memo[(row, col)]

        for i in range(n):
            dp(0, i)

        return [memo[(0, i)] for i in range(n)]
