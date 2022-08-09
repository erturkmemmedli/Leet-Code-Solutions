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
