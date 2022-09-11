class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        a, b, c = costs
        dp = [0] * (days[-1] + 1)
        index = 0
        for i in range(1, days[-1]+1):
            if days[index] == i:
                if i-30 >= 0:
                    dp[i] = min(dp[i-1] + a, dp[i-7] + b, dp[i-30] + c)
                elif i-7 >= 0:
                    dp[i] = min(dp[i-1] + a, dp[i-7] + b, c)
                else:
                    dp[i] = min(dp[i-1] + a, b, c)
                index += 1
            else:
                dp[i] = dp[i-1]
        return dp[-1]
