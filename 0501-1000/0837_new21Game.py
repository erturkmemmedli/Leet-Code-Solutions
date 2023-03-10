class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n > k + maxPts:
            return 1
        dp = [1] + [0] * n
        summ = 1
        for i in range(1, n + 1):
            dp[i] = summ / maxPts
            if i < k:
                summ += dp[i]
            if i >= maxPts:
                summ -= dp[i - maxPts]
        return sum(dp[k:])
