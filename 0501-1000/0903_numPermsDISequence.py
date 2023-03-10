class Solution:
    def numPermsDISequence(self, s: str) -> int:
        n = len(s)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            for j in range(i + 1):
                if s[i-1] == 'I':
                    dp[i][j] = sum(dp[i - 1][:j])
                if s[i-1] == 'D':
                    dp[i][j] = sum(dp[i - 1][j:i])
        return sum(dp[-1]) % 1_000_000_007
