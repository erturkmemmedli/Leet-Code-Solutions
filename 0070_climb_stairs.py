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
