class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]
        dp[0][0] = True

        for i in range(1, len(p) + 1):
            if p[i - 1] == '*':
                dp[i][0] |= dp[i - 1][0]

        for i in range(1, len(p) + 1):
            for j in range(1, len(s) + 1):
                if p[i - 1] == '*':
                    dp[i][j] = dp[i - 1][j - 1] or dp[i][j - 1] or dp[i - 1][j]

                elif p[i - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]

                else:
                    dp[i][j] = dp[i - 1][j - 1] and s[j - 1] == p[i - 1]

        return dp[-1][-1]
