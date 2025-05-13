class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mod = 1_000_000_007
        dp = [1] * 26 + [0] * 100_000

        for i in range(26, 100_026):
            dp[i] = (dp[i - 26] + dp[i - 26 + 1]) % mod
        
        return sum(dp[ord(c) - ord('a') + t] for c in s) % mod
