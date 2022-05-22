class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        if m == 0 or n == 0: return
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                dp[i][j] = self.dfs(matrix, m, n, dp, i, j)
        return max(self.dfs(matrix, m, n, dp, i, j) for i in range(m) for j in range(n))
        
    def dfs(self, matrix, m, n, dp, i, j):
        if not dp[i][j]:
            v = matrix[i][j]
            dp[i][j] = 1 + max(self.dfs(matrix, m, n, dp, i-1, j) if i and v < matrix[i-1][j] else 0,
                               self.dfs(matrix, m, n, dp, i+1, j) if i < m-1  and v < matrix[i+1][j] else 0,
                               self.dfs(matrix, m, n, dp, i, j-1) if j and v < matrix[i][j-1] else 0,
                               self.dfs(matrix, m, n, dp, i, j+1) if j < n-1  and v < matrix[i][j+1] else 0)
        return dp[i][j]
