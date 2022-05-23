class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for s in strs:
            M = s.count('0')
            N = s.count('1')
            for i in range(m, M - 1, -1):
                for j in range(n, N - 1, -1):
                    dp[i][j] = max(dp[i][j], 1 + dp[i - M][j - N])
        return dp[-1][-1]
