class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            dp[i][0] = i
        for j in range(1,n+1):
            dp[0][j] = j
        for i in range(1, m+1):
            for j in range(1, n+1):
                insert = dp[i-1][j] + 1
                delete = dp[i][j-1] + 1
                replace = dp[i-1][j-1] + 1
                no_change = dp[i-1][j-1]
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = min(insert, delete, no_change)
                else:
                    dp[i][j] = min(insert, delete, replace)
        return dp[-1][-1]

# Alternative solution

class Solution1:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            dp[i][0] = i
        for j in range(1,n+1):
            dp[0][j] = j
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = min(dp[i][j-1] + 1, dp[i-1][j] + 1, dp[i-1][j-1])
                else:
                    dp[i][j] = min(dp[i][j-1] + 1, dp[i-1][j] + 1, dp[i-1][j-1] + 1)
        return dp[-1][-1]
