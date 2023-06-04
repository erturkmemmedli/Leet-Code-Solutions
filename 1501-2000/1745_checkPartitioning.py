class Solution:
    def checkPartitioning(self, s: str) -> bool:
        n = len(s)
        memo = {}

        for i in range(2 * n - 1):
            low, high = i // 2, (i + 1) // 2

            while 0 <= low <= high < len(s) and s[low] == s[high]:
                if low not in memo:
                    memo[low] = set()

                memo[low].add(high)
                low -= 1
                high += 1

        @lru_cache(None)
        def dp(i, k):
            if k < 0:
                return False

            if i == n:
                return k == 0

            return any(dp(j + 1, k - 1) for j in memo[i])

        return dp(0, 3)
