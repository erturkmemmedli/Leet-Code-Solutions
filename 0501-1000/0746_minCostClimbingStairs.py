class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, len(cost)):
            dp[i] = min(dp[i-1] + cost[i], dp[i-2] + cost[i])
        return min(dp[-1], dp[-2])

# Alternative solution

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.memo = {}
        self.dp(cost, 0)
        return min(self.memo[0], self.memo[1])

    def dp(self, cost, index):
        if index >= len(cost):
            return 0

        if index in self.memo:
            return self.memo[index]

        self.memo[index] = cost[index] + min(self.dp(cost, index + 1), self.dp(cost, index + 2))
        return self.memo[index]
