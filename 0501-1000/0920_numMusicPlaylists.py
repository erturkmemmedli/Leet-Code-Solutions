class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        mod = 10 ** 9 + 7
        dp = [[0 for _ in range(n+1)] for _ in range(goal+1)]
        dp[1][1] = 1
        for i in range(2, goal+1):
            for j in range(1, min(n+1, i+1)):
                dp[i][j] = (dp[i][j] + dp[i-1][j-1] * j) % mod
                if j > k:
                    dp[i][j] = (dp[i][j] + dp[i-1][j] * (j-k)) % mod
        return dp[-1][-1]
