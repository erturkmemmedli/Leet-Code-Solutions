class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = max(dp[i-1][j-1] + 1, dp[i][j-1], dp[i-1][j])
                else:
                    dp[i][j] = max(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])
        return dp[-1][-1]


# Alternative solution

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n+1) for _ in range(m+1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i-1][j-1] + 1 if text1[i-1] == text2[j-1] else max(dp[i-1][j], dp[i][j-1])

        self.subsequence = ""
        self.reconstruct_path(dp, text1, text2, m, n)
        print('longest common subsequence: ', self.subsequence[::-1])

        return dp[m][n]

    def reconstruct_path(self, dp, s1, s2, row, col):
        if row == 0 or col == 0:
            return

        if dp[row-1][col-1] == dp[row][col]:
            return self.reconstruct_path(dp, s1, s2, row-1, col-1)

        elif dp[row-1][col] == dp[row][col]:
            return self.reconstruct_path(dp, s1, s2, row-1, col)
        
        elif dp[row][col-1] == dp[row][col]:
            return self.reconstruct_path(dp, s1, s2, row, col-1)

        else:
            self.subsequence += s1[row-1]
            return self.reconstruct_path(dp, s1, s2, row-1, col-1)
        
