class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        if m == 0 or n == 0: return
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                dp[i][j] = self.dfs(matrix, m, n, dp, i, j)
        return max(dp[i][j] for i in range(m) for j in range(n))
        
    def dfs(self, matrix, m, n, dp, i, j):
        if not dp[i][j]:
            v = matrix[i][j]
            dp[i][j] = 1 + max(self.dfs(matrix, m, n, dp, i-1, j) if i and v < matrix[i-1][j] else 0,
                               self.dfs(matrix, m, n, dp, i+1, j) if i < m-1  and v < matrix[i+1][j] else 0,
                               self.dfs(matrix, m, n, dp, i, j-1) if j and v < matrix[i][j-1] else 0,
                               self.dfs(matrix, m, n, dp, i, j+1) if j < n-1  and v < matrix[i][j+1] else 0)
        return dp[i][j]
    
# Alternative solution

class Solution1:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]

        def dfs(i, j):
            if not dp[i][j]:
                for row, col in [i-1, j], [i+1, j], [i, j-1], [i, j+1]:
                    if m > row >= 0 <= col < n and matrix[row][col] < matrix[i][j]:
                        dp[i][j] = max(dp[i][j], 1 + dfs(row, col))
            return dp[i][j] if dp[i][j] else 1

        for i in range(m):
            for j in range(n):
                dp[i][j] = dfs(i, j)
        return max(dp[i][j] for i in range(m) for j in range(n))

# Alternative solution (which gives TLE error)

class Solution2:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[1] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                self.dfs(matrix, m, n, dp, i, j)
        return max(dp[i][j] for i in range(m) for j in range(n))

    def dfs(self, mat, m, n, dp, i, j):
        for row, col in [i-1, j], [i+1, j], [i, j-1], [i, j+1]:
            if m > row >= 0 <= col < n and mat[row][col] > mat[i][j]:
                dp[row][col] = max(dp[row][col], dp[i][j] + 1)
                self.dfs(mat, m, n, dp, row, col)
        return
    
# Alternative solution (which gives TLE error)

class Solution3:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[1] * n for _ in range(m)]

        def dfs(i, j):
            for row, col in [i-1, j], [i+1, j], [i, j-1], [i, j+1]:
                if m > row >= 0 <= col < n and matrix[row][col] > matrix[i][j]:
                    dp[row][col] = max(dp[row][col], dp[i][j] + 1)
                    dfs(row, col)
            return        

        for i in range(m):
            for j in range(n):
                dfs(i, j)
        return max(dp[i][j] for i in range(m) for j in range(n))
