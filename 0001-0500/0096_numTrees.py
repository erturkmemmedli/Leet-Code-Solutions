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

# Alternative solution

class Solution:
    def numTrees(self, n: int) -> int:
        memo = {}

        def dp(n):
            if n == 0:
                return 1
            
            if n in memo:
                return memo[n]

            res = 0

            for i in range(n):
                if i != n - i - 1:
                    res += dp(i) * dp(n - i - 1)
                else:
                    res += dp(i) ** 2
            
            memo[n] = res
            return res
        
        return dp(n)

# Alternative solution

class Solution:
    def numTrees(self, n: int) -> int:
        return factorial(2 * n) // factorial(n + 1) // factorial(n)
