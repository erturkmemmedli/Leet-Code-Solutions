class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs[0])
        dp = [1] * n
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                if all(string[i] <= string[j] for string in strs):
                    dp[i] = max(dp[i], dp[j] + 1)
        return n - max(dp)
