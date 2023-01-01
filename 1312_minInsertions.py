class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        l = self.lcs(n, s, s[::-1])
        return n - l

    def lcs(self, n, s1, s2):
        dp = [0 for _ in range(n+1)]
        for i in range(1, n+1):
            row = [0]
            for j in range(1, n+1):
                if s1[i-1] == s2[j-1]:
                    row.append(dp[j-1] + 1)
                else:
                    row.append(max(dp[j-1], row[j-1], dp[j]))
            dp = row
        return max(dp)
