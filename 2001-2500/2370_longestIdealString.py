class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        hashmap = [0] * 26

        for char in s:
            i = ord(char) - ord('a')
            hashmap[i] = max(hashmap[max(0, i - k) : min(25, i + k) + 1]) + 1

        return max(hashmap)

# Alternative solution (which gives TLE error)

class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [1] * len(s)

        for i in range(1, len(s)):
            for j in range(i):
                if abs(ord(s[i]) -ord(s[j])) <= k:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
