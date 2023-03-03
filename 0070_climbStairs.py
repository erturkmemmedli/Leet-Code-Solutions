class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1
        if n > 1: dp[2] = 2
        for i in range(3, n + 1): dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]

# Alternative solution

class Solution1:
    def climbStairs(self, n: int) -> int:
        if n < 3: return n
        prev = 1
        answer = 2
        for i in range(3, n + 1):
            prev, answer = answer, answer + prev
        return answer

# Alternative solution

class Solution2:
    def climbStairs(self, n: int) -> int:
        prev = 0
        next = 1
        for _ in range(n):
            prev, next = next, prev+next
        return next

# Alternative solution

class Solution:
    def climbStairs(self, n: int) -> int:
        self.memo = {}
        return self.dp(n)

    def dp(self, n):
        if n == 0:
            return 1
        
        if n < 0:
            return 0

        if n in self.memo:
            return self.memo[n]

        self.memo[n] = self.dp(n-1) + self.dp(n-2)
        return self.memo[n]
