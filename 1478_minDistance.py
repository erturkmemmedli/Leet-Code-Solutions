class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        n = len(houses)
        houses.sort()
        costs = [[0] * n for _ in range(n)]
        for i, j in itertools.product(range(n), range(n)):
            median = houses[(i+j)//2]
            for d in range(i, j + 1):
                costs[i][j] += abs(median - houses[d])
        dp = [[float("inf")] * k for _ in range(n)]
        for i in range(n):
            dp[i][0] = costs[0][i]
        for x in range(1, k):
            for i in range(n):
                for j in range(i):
                    dp[i][x] = min(dp[i][x], dp[j][x-1] + costs[j+1][i])
        return dp[-1][-1]
