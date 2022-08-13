class Solution:
    def numTrees(self, n: int) -> int:
        dp = [1, 1]
        for i in range(2, n+1):
            addition = 0
            right = i - 1
            left = 0
            while left <= right:
                if left < right:
                    addition += 2 * dp[right] * dp[left]
                if left == right:
                    addition += dp[right] * dp[left]
                left += 1
                right -= 1
            dp.append(addition)
        return dp[-1]
