class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 2, -1, -1):
            for j in range(i + 2, n):
                dp[i][j] = max(nums[i] * nums[j] * nums[k] + dp[i][k] + dp[k][j] for k in range(i + 1, j))
        return dp[0][-1]

# Alternative solution

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        for i in range(n-2, -1, -1):
            for j in range(i + 2, n):
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], nums[i] * nums[j] * nums[k] + dp[i][k] + dp[k][j])
        
        return dp[0][-1]

# Alternative solution

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        memo = {}

        def dp(left, right):
            if left > right:
                return 0

            if (left, right) in memo:
                return memo[(left, right)]

            memo[(left, right)] = 0

            for i in range(left, right + 1):
                coin = nums[i] * nums[left - 1] * nums[right + 1] + dp(left, i - 1) + dp(i + 1, right)
                memo[(left, right)] = max(memo[(left, right)], coin)

            return memo[(left, right)]
        
        return dp(1, len(nums) - 2)
