class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for i in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]    

# Alternative solution

class Solution1:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        for i in range(m-1):
            for j in range(1, n):
                dp[j] = dp[j-1] + dp[j]
        return dp[-1]

# Alternative solution

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        self.memo = {}
        return self.dp(m, n, 0, 0)

    def dp(self, m, n, row, col):
        if row == m-1 and col == n-1:
            return 1

        if row == m or col == n:
            return 0

        if (row, col) in self.memo:
            return self.memo[(row, col)]

        self.memo[(row, col)] = self.dp(m, n, row + 1, col) + self.dp(m, n, row, col + 1)
        return self.memo[(row, col)]
